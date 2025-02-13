import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Definir o endereço e a porta do servidor
server_address = ('localhost', 4443)

# Criar o servidor
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Carregar o certificado e a chave privada
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="./server.key",  # Caminho da chave privada
                               certfile="./server.crt",  # Caminho do certificado
                               server_side=True)

print("Servidor HTTPS rodando em https://localhost:4443")
httpd.serve_forever()
