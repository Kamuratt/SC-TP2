# Projeto de Servidor e Cliente HTTPS

Este projeto implementa um servidor HTTPS e um cliente que realiza requisições seguras para este servidor. O servidor foi configurado para utilizar um certificado autoassinado gerado com o algoritmo RSA e a biblioteca `cryptography`. A comunicação entre o cliente e o servidor é garantida com criptografia TLS/SSL, utilizando o protocolo HTTPS.

## Bibliotecas e Ferramentas Utilizadas

- **Python**: 3.11.7
- **ssl**: 3.0.13
- **requests**: 2.32.3
- **cryptography**: 44.0.1
- **OpenSSL**: 3.0.13

Essas bibliotecas foram essenciais para a implementação do servidor e cliente HTTPS, incluindo a criptografia simétrica e assimétrica, a geração de chaves, o hash de certificados e a criação de conexões seguras.

## Protocolos e Algoritmos Utilizados

- **HTTPS/TLS**: O servidor foi configurado para usar o protocolo HTTPS, que por sua vez, usa o protocolo TLS para garantir a criptografia da comunicação entre cliente e servidor.
  
- **RSA**: O certificado foi gerado com o algoritmo RSA (Rivest–Shamir–Adleman), utilizado para a criptografia assimétrica que assegura a troca segura de informações.

- **SHA-256**: O hash SHA-256 foi utilizado no processo de assinatura do certificado, garantindo a integridade e autenticidade da comunicação.

## Como Rodar o Projeto

Para rodar o servidor e o cliente localmente, siga os passos abaixo:

1. Clone o repositório para o seu diretório local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Crie e ative um ambiente virtual para instalar as dependências (recomendado):
  ```bash
  python -m venv .venv
  ```
  ```bash
  source .venv/bin/activate   # Para sistemas Unix-based
  ```
  ```bash
  .venv\Scripts\activate      # Para Windows
  ```
3. Instale as dependências: 
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```bash
   python Servidor.py
   ```
5. Em outro terminal, execute o cliente para fazer uma requisição HTTPS ao servidor:
   ```bash
   python requisicao.py
   ```
