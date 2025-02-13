# Projeto de Servidor e Cliente HTTPS

## Bibliotecas e Ferramentas Utilizadas

- **Python**: 3.11.7
- **ssl**: 3.0.13
- **requests**: 2.32.3
- **cryptography**: 44.0.1
- **OpenSSL**: 3.0.13
## Descrição do Projeto

Este projeto implementa um servidor HTTPS e um cliente que realiza requisições seguras para este servidor. O servidor utiliza um certificado autoassinado gerado com o algoritmo RSA e a biblioteca `cryptography`. A comunicação entre cliente e servidor é garantida com criptografia TLS/SSL, utilizando o protocolo HTTPS.
