import ssl
import socket
import logging
from h2.connection import H2Connection
from h2.events import ResponseReceived, DataReceived

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Criar contexto SSL e confiar no certificado do servidor autoassinado
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='./server.crt')  # Certificado do servidor
context.set_alpn_protocols(['h2'])  # Define HTTP/2

# Criar conexão segura com o servidor
conn = socket.create_connection(('localhost', 4433))
ssl_conn = context.wrap_socket(conn, server_hostname='localhost')

logging.info("Conexão SSL estabelecida com autenticação do servidor!")

# Verificar o certificado do servidor (autoassinado)
peer_cert = ssl_conn.getpeercert()
logging.info(f"Certificado do servidor: {peer_cert}")

# Comparar o certificado do servidor com o esperado (autoassinado)
subject = peer_cert.get('subject', [])
common_name = None

# Percorrer a tupla de tuplas no subject
for field in subject:
    if field[0][0] == 'commonName':
        common_name = field[0][1]
        break

# Comparar 'commonName' com o valor esperado
if common_name == 'localhost':
    logging.info("Certificado do servidor corresponde ao esperado!")
else:
    logging.error("Certificado do servidor NÃO corresponde ao esperado!")

# Configurar conexão HTTP/2
h2_conn = H2Connection()
h2_conn.initiate_connection()
ssl_conn.sendall(h2_conn.data_to_send())

# Enviar requisição HTTP/2
headers = [
    (':method', 'GET'),
    (':path', '/'),
    (':scheme', 'https'),
    (':authority', 'localhost'),
]
h2_conn.send_headers(1, headers, end_stream=True)
ssl_conn.sendall(h2_conn.data_to_send())

# Receber resposta
while True:
    data = ssl_conn.recv(65535)
    if not data:
        break

    # Processar os dados recebidos
    events = h2_conn.receive_data(data)  # Recebe e processa os dados

    # Agora processa cada evento gerado
    for event in events:
        if isinstance(event, ResponseReceived):
            logging.info(f"Resposta recebida: {event.headers}")
        elif isinstance(event, DataReceived):
            logging.info(f"Corpo da resposta: {event.data.decode('utf-8')}")

# Fechar conexão
ssl_conn.close()
conn.close()
logging.info("Conexão fechada.")
