## Arquivo: servidor.py
import os
import logging
import ssl
import socket
from h2.connection import H2Connection
from h2.events import RequestReceived, DataReceived
from dotenv import load_dotenv
from Criação_de_Certificado import gerar_certificado

# Carregar variáveis de ambiente
load_dotenv()
SENHA_CERTIFICADO = os.getenv("CERT_PASSWORD")

# Configuração de logging
logging.basicConfig(level=logging.INFO)

def iniciar_servidor():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key', password=SENHA_CERTIFICADO.encode())
    context.set_alpn_protocols(['h2'])
    context.minimum_version = ssl.TLSVersion.TLSv1_3
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 4433))
    server_socket.listen(5)
    logging.info("Servidor HTTPS/2 aguardando conexões em https://localhost:4433")

    while True:
        client_socket, addr = server_socket.accept()
        logging.info(f"Conexão recebida de {addr}")

        try:
            ssl_socket = context.wrap_socket(client_socket, server_side=True)
            logging.info("Conexão SSL estabelecida!")

            if ssl_socket.selected_alpn_protocol() != 'h2':
                logging.error("Protocolo negociado não é HTTP/2!")
                ssl_socket.close()
                continue

            h2_conn = H2Connection()
            h2_conn.initiate_connection()
            ssl_socket.sendall(h2_conn.data_to_send())

            while True:
                data = ssl_socket.recv(65535)
                if not data:
                    break
                
                events = h2_conn.receive_data(data)
                for event in events:
                    if isinstance(event, RequestReceived):
                        logging.info(f"Recebida requisição: {event.headers}")
                        
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
            if ssl_socket:
                ssl_socket.close()
            client_socket.close()

if __name__ == "__main__":
    if not os.path.exists("server.crt") or not os.path.exists("server.key"):
        gerar_certificado()
    iniciar_servidor()