# Projeto de Servidor e Cliente HTTPS

## Bibliotecas e Ferramentas Utilizadas

- **Python**: `3.x.x` (Verifique com `python --version`)
- **ssl** (módulo integrado ao Python, versão do OpenSSL: `OpenSSL 1.x.x`)
- **requests**: `x.x.x` (Obtido com `pip show requests`)
- **cryptography**: `x.x.x` (Obtido com `pip show cryptography`)
- **OpenSSL**: `1.x.x` (Caso tenha sido instalado localmente, use `openssl version` para verificar)

## Descrição do Projeto

Este projeto implementa um servidor HTTPS e um cliente que realiza requisições seguras para este servidor. O servidor utiliza um certificado autoassinado gerado com o algoritmo RSA e a biblioteca `cryptography`. A comunicação entre cliente e servidor é garantida com criptografia TLS/SSL, utilizando o protocolo HTTPS.
