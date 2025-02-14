import ssl
import socket
import logging
from h2.connection import H2Connection
from h2.events import RequestReceived, DataReceived

# Senha global para garantir o acesso ao servidor e ao cliente
senha_gerada = "VxG$7t@4pL8M1jR#f3D9&zQzK$LwQ@t2"  # Senha fixa definida anteriormente

# Configuração do log
logging.basicConfig(level=logging.INFO)

# Criar contexto SSL com configurações de segurança
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='./server.crt', keyfile='./server.key', password=bytes(senha_gerada, 'utf-8'))  # Usando a senha fixa para carregar a chave privada
context.load_verify_locations('./server.crt')  # O servidor confia no próprio certificado
context.verify_mode = ssl.CERT_NONE  # Cliente NÃO precisa apresentar certificado
context.set_alpn_protocols(['h2'])  # Define HTTP/2

# Forçar uso exclusivo de TLS 1.3 e desabilitar ciphers antigos
context.set_ciphers('ALL')  # Exemplo de ciphers seguros para TLS 1.3
context.minimum_version = ssl.TLSVersion.TLSv1_3  # Garantir que TLS 1.3 seja o mínimo
context.maximum_version = ssl.TLSVersion.TLSv1_3  # Garantir que TLS 1.3 seja o máximo

# Criar e configurar socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 4433))
server_socket.listen(5)

logging.info("Servidor HTTPS/2 aguardando conexões em https://localhost:4433")

while True:
    client_socket, addr = server_socket.accept()
    logging.info(f"Conexão recebida de {addr}")

    ssl_socket = None  # Garantir que a variável existe antes do try

    try:
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
        logging.info("Conexão SSL estabelecida!")

        # Verificar se o protocolo HTTP/2 foi negociado
        alpn_protocol = ssl_socket.selected_alpn_protocol()
        if alpn_protocol != 'h2':
            logging.error(f"Erro: protocolo não suportado, esperado 'h2', mas foi negociado '{alpn_protocol}'")
            ssl_socket.close()
            continue

        # Inicializar conexão HTTP/2
        h2_conn = H2Connection()
        h2_conn.initiate_connection()
        ssl_socket.sendall(h2_conn.data_to_send())

        # Processar requisição
        while True:
            data = ssl_socket.recv(65535)
            if not data:
                break

            # Processar os dados recebidos
            events = h2_conn.receive_data(data)  # Recebe e processa os dados

            # Agora processa cada evento gerado
            for event in events:
                if isinstance(event, RequestReceived):
                    logging.info(f"Recebida requisição: {event.headers}")

                    # Responder com HTTP/2
                    response_headers = [
                        (':status', '200'),
                        (':scheme', 'https'),
                        ('content-type', 'text/plain'),
                    ]
                    h2_conn.send_headers(event.stream_id, response_headers)
                    h2_conn.send_data(event.stream_id, "Conexão bem sucedida e segura".encode('utf-8'), end_stream=True)

                    ssl_socket.sendall(h2_conn.data_to_send())

    except ssl.SSLError as e:
        logging.error(f"Erro SSL no servidor: {e}")
    except Exception as e:
        logging.error(f"Erro no servidor: {e}")
    finally:
        # Garantir o fechamento do socket, se existir
        if ssl_socket:
            ssl_socket.close()
        client_socket.close()
