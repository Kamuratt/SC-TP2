# Projeto de Servidor e Cliente HTTPS

Este projeto implementa um servidor HTTPS e um cliente que realiza requisições seguras para esse servidor. A comunicação entre o cliente e o servidor é realizada com segurança, utilizando criptografia TLS/SSL, que garante a confidencialidade e integridade dos dados transmitidos. O servidor foi configurado para utilizar um **certificado autoassinado** gerado com o algoritmo **RSA**, utilizando a biblioteca `cryptography` para gerar chaves criptográficas e o certificado.

A implementação também inclui a configuração do protocolo **HTTP/2** para melhorar o desempenho e a eficiência na comunicação entre cliente e servidor. O projeto foi desenvolvido com foco em segurança, adotando as melhores práticas na configuração do SSL/TLS.

## Bibliotecas e Ferramentas Utilizadas

- **Python**: 3.11.7  
  A versão utilizada do Python foi escolhida devido à sua estabilidade e compatibilidade com as bibliotecas utilizadas no projeto.

- **ssl**: 3.0.13  
  Biblioteca padrão do Python utilizada para configurar as conexões seguras TLS/SSL, incluindo verificação de certificados, criptografia e suporte ao protocolo HTTPS.

- **requests**: 2.32.3  
  Biblioteca para facilitar a realização de requisições HTTP/HTTPS, garantindo a comunicação segura com o servidor.

- **cryptography**: 44.0.1  
  Biblioteca utilizada para geração de chaves RSA, criação de certificados digitais e criptografia de dados. Ela foi essencial para criar o certificado autoassinado utilizado na comunicação segura.

- **OpenSSL**: 3.0.13  
  Utilizado para manipulação de certificados e para fornecer suporte para geração de chaves e outros processos relacionados à criptografia.

Essas bibliotecas desempenham um papel essencial na implementação do servidor e cliente HTTPS, incluindo a geração de chaves públicas e privadas, assinatura e verificação de certificados, e comunicação segura utilizando o protocolo TLS.

## Protocolos e Algoritmos Utilizados

- **HTTPS/TLS**:  
  O servidor foi configurado para utilizar o protocolo HTTPS, que por sua vez, utiliza o protocolo TLS (Transport Layer Security) para garantir a criptografia da comunicação entre cliente e servidor. O uso do TLS assegura a confidencialidade e a integridade dos dados durante a transmissão.

- **RSA**:  
  O certificado utilizado foi gerado com o algoritmo **RSA** (Rivest-Shamir-Adleman), um dos mais utilizados na criptografia assimétrica. A chave privada RSA de **4096 bits** foi utilizada para assinar o certificado e criptografar a comunicação, garantindo que apenas o destinatário correto pudesse descriptografá-la.

- **SHA-256**:  
  O algoritmo **SHA-256** foi utilizado para a criação do hash que assina o certificado digital. O SHA-256 assegura a integridade do certificado, permitindo verificar se ele foi modificado durante o tráfego. Ele é fundamental para a construção de uma cadeia de confiança.

- **HTTP/2**:  
  O protocolo **HTTP/2** foi configurado para otimizar a comunicação entre cliente e servidor, permitindo multiplexação, compressão de cabeçalhos e outras melhorias em relação ao HTTP/1.1. Isso resulta em uma comunicação mais eficiente e rápida, reduzindo o tempo de resposta do servidor.

## Detalhamento da Criação do Certificado e Configuração do Servidor

### Criação do Certificado

O certificado utilizado é autoassinado, ou seja, não foi emitido por uma autoridade certificadora (CA), mas sim gerado localmente para fins de teste e desenvolvimento. O processo de criação do certificado envolveu as seguintes etapas:

1. **Geração de Chave Privada**:  
   Utilizando o algoritmo RSA, uma chave privada de **4096 bits** foi gerada.

2. **Criptografia da Chave Privada**:  
   A chave privada foi criptografada com a senha fixa **"VxG$7t@4pL8M1jR#f3D9&zQzK$LwQ@t2"** para maior segurança.

3. **Criação do Certificado Autoassinado**:  
   O certificado foi gerado com um período de validade de **1 ano**, utilizando o hash SHA-256 para assinar o certificado e garantir sua integridade. A configuração do certificado inclui o **common name** (CN) como "localhost", o que é esperado tanto no servidor quanto no cliente.

### Configuração do Servidor HTTPS

O servidor foi configurado para escutar na porta **4433** e foi configurado para aceitar conexões seguras utilizando o **TLS 1.3**, além de garantir que apenas ciphers seguros fossem utilizados. As principais configurações incluem:

- **Certificado e Chave Privada**:  
  O servidor carrega o certificado e a chave privada gerados anteriormente.

- **Verificação de Certificado**:  
  O servidor não exige que o cliente forneça um certificado, mas confia no seu próprio certificado autoassinado para validar a conexão.

- **Protocolo HTTP/2**:  
  O servidor foi configurado para utilizar o protocolo HTTP/2, com suporte a multiplexação e cabeçalhos comprimidos.

- **TLS 1.3 e Ciphers Seguros**:  
  O servidor foi configurado para utilizar exclusivamente o **TLS 1.3** e ciphers seguros para garantir uma comunicação segura e moderna.

## Como Rodar o Projeto

Para rodar o servidor e o cliente localmente, siga os passos abaixo:

1. **Clone o repositório** para o seu diretório local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
2. Crie e ative um ambiente virtual para instalar as dependências (recomendado):
  
  ```bash
  python -m venv .venv
```

Para sistemas Unix-based:

```bash
source .venv/bin/activate
```

Para sistemas Windows:

```bash
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```
4. Execute o servidor:

Inicie o servidor HTTPS na porta 4433, utilizando o seguinte comando:

```bash
python Servidor.py
```

5.Execute o cliente para fazer uma requisição HTTPS ao servidor:

Em outro terminal, execute o cliente para estabelecer a conexão e verificar o funcionamento do protocolo HTTPS com o servidor:

```bash
python requisicao.py
```

## Funcionamento do Cliente e Servidor

### Funcionamento do Cliente

1. **Conexão com o Servidor**:  
   O cliente estabelece uma conexão segura com o servidor, utilizando o certificado autoassinado gerado previamente. A comunicação é protegida pelo protocolo **TLS 1.3** e usa o protocolo **HTTP/2** para garantir uma troca de dados eficiente e segura.

2. **Requisição e Resposta**:  
   O cliente envia uma requisição `GET` ao servidor, solicitando uma página. Após a negociação TLS e autenticação, o servidor processa a requisição e responde com um código de status HTTP 200, confirmando que a conexão foi estabelecida com sucesso.

3. **Exibição de Resultados**:  
   A resposta do servidor é exibida no terminal, incluindo o conteúdo da resposta, como "Conexão bem sucedida e segura".

### Funcionamento do Servidor

1. **Escuta na Porta 4433**:  
   O servidor é configurado para escutar conexões na porta **4433**, esperando requisições HTTPS.

2. **Negociação TLS/SSL**:  
   Quando o cliente tenta se conectar, o servidor inicia a negociação TLS/SSL, validando o certificado autoassinado. Após a autenticação, o servidor assegura que a comunicação será criptografada e segura.

3. **Processamento da Requisição HTTP/2**:  
   O servidor processa a requisição HTTP/2 enviada pelo cliente, que pode incluir múltiplas solicitações simultâneas, graças à multiplexação do protocolo.

4. **Resposta ao Cliente**:  
   O servidor responde ao cliente com uma mensagem de sucesso, incluindo um código de status HTTP 200 e um corpo contendo a mensagem "Conexão bem sucedida e segura", indicando que a comunicação foi estabelecida com sucesso e de forma segura.

## Conclusão

Este projeto demonstra a implementação de um **servidor e cliente HTTPS seguros**, utilizando o **TLS 1.3** para criptografar a comunicação. O servidor foi configurado para trabalhar com um **certificado autoassinado RSA** e utiliza o **algoritmo SHA-256** para garantir a integridade e autenticidade dos dados transmitidos. Além disso, o servidor e o cliente utilizam **HTTP/2** para melhorar o desempenho da comunicação.

A implementação busca fornecer uma base sólida para a construção de sistemas de comunicação segura, com foco em criptografia, autenticação e performance. O projeto pode ser expandido para incluir autenticação mútua (mTLS), suporte a protocolos mais antigos ou novos, e outras funcionalidades de segurança.

