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

- **H2**: 4.2.0  
  Implementação do protocolo HTTP/2 para Python, permitindo o uso de múltiplas requisições em uma única conexão TCP, melhorando a eficiência e a performance da comunicação HTTP no projeto.

- **dotenv**: 1.0.1  
  Biblioteca utilizada para gerenciar variáveis de ambiente em arquivos `.env`, facilitando a configuração e o armazenamento seguro de informações sensíveis no projeto, como chaves de API e credenciais.

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

# Testes Realizados

## Análise de Segurança: Teste de Ciphers TLSv1.3 com Nmap

O teste foi realizado utilizando o seguinte comando:

```bash
nmap --script ssl-enum-ciphers -p 4433 localhost

```

### Resultado
```bash
PORT     STATE SERVICE
4433/tcp open  vop
| ssl-enum-ciphers: 
|   TLSv1.3: 
|     ciphers: 
|       TLS_AKE_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_AKE_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
|       TLS_AKE_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|     cipher preference: server
|_  least strength: A
```
## Ciphers Disponíveis para TLSv1.3

O script **ssl-enum-ciphers** listou três ciphers disponíveis para o protocolo **TLSv1.3**, todos com a classificação de segurança **A**. Eles são:

- **TLS_AKE_WITH_AES_256_GCM_SHA384 (ecdh_x25519)**: Usa **AES-256** com Galois/Counter Mode (GCM) e SHA-384.
- **TLS_AKE_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519)**: Usa o **ChaCha20**, um cipher de fluxo altamente seguro, com SHA-256.
- **TLS_AKE_WITH_AES_128_GCM_SHA256 (ecdh_x25519)**: Usa **AES-128** com GCM e SHA-256.

Esses ciphers são todos recomendados para conexões seguras, pois utilizam algoritmos modernos e eficientes de criptografia, como **AES** e **ChaCha20**, que são resilientes contra ataques comuns. A curva de troca de chave **x25519** é altamente segura e eficiente, sendo considerada uma das melhores opções para troca de chaves públicas no contexto de TLS.

## Classificação de Segurança

Todos os ciphers têm a classificação **A**, o que significa que estão na faixa mais segura, segundo as melhores práticas de segurança para **TLSv1.3**. Essa classificação indica que não há ciphers fracos ou vulneráveis sendo utilizados, o que é fundamental para garantir a confidencialidade e integridade da comunicação.

### Cipher Preference

O servidor está configurado para **escolher automaticamente os melhores ciphers** disponíveis, o que é uma prática recomendada, pois garante que o servidor sempre priorize os ciphers mais seguros e modernos durante o processo de negociação.

### Least Strength

O teste também indicou que a **menor força de segurança** (least strength) entre os ciphers é **A**, o que confirma que todos os ciphers fornecidos são altamente seguros.

## Resumo

O servidor está configurado para utilizar apenas ciphers fortes e modernos para o protocolo **TLSv1.3**. A presença de ciphers com **AES-256** e **ChaCha20**, além da curva **x25519**, indica que o servidor está aderindo às melhores práticas de segurança para criptografia de dados. A classificação "**A**" confirma que a configuração de segurança é sólida e não apresenta vulnerabilidades óbvias associadas ao uso de ciphers fracos ou obsoletos.

## Análise Técnica do Teste: openssl s_client -connect localhost:4433 -tls1_3 -servername localhost -CAfile "./server.crt"

### 1. Detalhes do Certificado

O servidor utiliza um **certificado autoassinado**. A verificação de certificado foi bem-sucedida, com o **certificado válido** dentro do período de validade:

- **NotBefore**: Feb 16 16:37:57 2025 GMT
- **NotAfter**: Feb 16 16:38:57 2026 GMT

### Informações do Certificado:
- **Emissor e Assinante**: O certificado foi assinado pela mesma entidade (self-signed) com os dados:
  - **C = BR** (País: Brasil)
  - **ST = São Paulo** (Estado)
  - **O = Minha Empresa** (Organização)
  - **CN = localhost** (Nome Comum)
- **Chave Pública**: 4096 bits, usando o algoritmo RSA.

A verificação do certificado foi concluída com sucesso (retorno `Verify return code: 0 (ok)`), o que indica que o certificado foi aceito como válido pelo cliente.

## 2. Handshake SSL/TLS

O **SSL handshake** foi completado com sucesso. Durante o handshake, os dados foram lidos e gravados sem problemas:

- **Bytes lidos**: 2221
- **Bytes gravados**: 323

O protocolo de handshake utilizado foi o **TLSv1.3**, a versão mais recente e segura do protocolo TLS.

## 3. Cifra Usada

A **cifra TLS** negociada para a sessão foi o `TLS_AES_256_GCM_SHA384`, que é uma cifra moderna e segura, com as seguintes características:

- **AES-256**: Usando o algoritmo de criptografia AES com chave de 256 bits.
- **GCM (Galois/Counter Mode)**: Um modo de operação de cifra autenticada, fornecendo tanto confidencialidade quanto integridade.
- **SHA-384**: Usando o algoritmo de hash SHA-384 para a geração de um valor de resumo de 384 bits.

Essa cifra é adequada para garantir a segurança e integridade da comunicação.

## 4. Detalhes de Sessão

Foi estabelecida uma **sessão TLS** com as seguintes características:

- **ID da Sessão**: `BB66887CAF35195630DDFBFC216A73711CD065A07C9C499D09BF1DBB26820105`
- **Chave Pública do Servidor**: 4096 bits
- **Renegociação Segura**: Não suportada
- **Compressão**: Nenhuma
- **Expansão**: Nenhuma
- **Protocolo**: TLSv1.3
- **Cifra**: TLS_AES_256_GCM_SHA384

A sessão também usou **Tickets de Sessão**, uma técnica de otimização para evitar a necessidade de um novo handshake em futuras conexões com o mesmo servidor.

## 5. Informações do Ticket de Sessão

O servidor enviou um **Ticket de Sessão**, permitindo a reutilização de sessões TLS em futuras conexões sem a necessidade de refazer o handshake completo. Isso ajuda a melhorar a performance, especialmente em ambientes de alta carga.

O ticket contém os seguintes detalhes:

- **Tempo de vida do Ticket**: 7200 segundos (2 horas)
- **Sessão PSK (Pre-Shared Key)**: Usada para a ressumação da sessão, garantindo que a comunicação continue de onde parou sem a necessidade de re-negociar as chaves.

## 6. Resumo de Segurança

Este teste mostra que o servidor está utilizando um **certificado autoassinado**, mas o cliente aceitou o certificado sem erros, o que é um bom indicativo de que o servidor está configurado corretamente para a validação do certificado. A cifra TLS AES-256-GCM-SHA384 é robusta, garantindo a confidencialidade e integridade da comunicação.

Além disso, a utilização de **sessões com tickets** permite otimizar as conexões subsequentes, reduzindo o tempo de negociação do protocolo e melhorando a performance.

## 7. Considerações Finais

- A conexão TLS foi estabelecida com sucesso usando **TLSv1.3**, a versão mais segura do protocolo.
- O **certificado autoassinado** foi aceito sem problemas, embora o uso de certificados assinados por uma autoridade confiável seja recomendado para produção.
- A **cifra** utilizada é moderna e segura.
- **Tickets de Sessão** estão habilitados, o que otimiza a reconexão.

Esse teste confirma que a configuração do servidor está implementando boas práticas de segurança para a comunicação HTTPS utilizando TLS 1.3.

# Análise Técnica do Teste: `openssl s_client -connect localhost:4433 -tls1_2`

## 1. Resultado do Servidor

O servidor registrou o seguinte erro ao tentar estabelecer uma conexão usando **TLS 1.2**:

ERROR:root:Erro SSL no servidor: [SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:1006)


Este erro indica que o servidor **não suporta TLS 1.2** para a porta em questão, resultando na recusa da conexão.

## 2. Resultado do Teste no Cliente

O cliente recebeu a seguinte mensagem de erro durante o teste:

CONNECTED(000001C4) 9C720000:error:0A00042E:SSL routines:ssl3_read_bytes:tlsv1 alert protocol version:ssl\record\rec_layer_s3.c:1590:SSL alert number 70


Este erro é gerado pelo cliente, indicando que a tentativa de estabelecer uma conexão com **TLS 1.2** falhou devido à versão do protocolo não ser suportada pelo servidor. O número de alerta `70` corresponde ao erro de versão do protocolo.

### Detalhes do Resultado:

- **Sem certificado de peer**: Não houve certificado apresentado pelo servidor.
- **Sem certificado de cliente**: O cliente não enviou um certificado de CA.
- **Handshake SSL**: O handshake tentou ser realizado, mas resultou em falha devido à versão do protocolo.
    - Bytes lidos: 7
    - Bytes escritos: 188

O teste mostra que o servidor não suporta **TLS 1.2** e, como resultado, a conexão foi recusada.

## 3. Detalhes da Sessão SSL/TLS

Apesar da falha na negociação do protocolo, as informações da sessão SSL são apresentadas:

- **Protocolo**: TLSv1.2
- **Cifra**: Nenhuma (`0000`), indicando que a negociação de cifra falhou.
- **Sessão**: Nenhuma sessão foi estabelecida, pois a conexão foi interrompida antes de qualquer negociação efetiva.
- **Renegociação Segura**: Não suportada.
- **Compressão**: Nenhuma.
- **Expansão**: Nenhuma.
- **ALPN (Application-Layer Protocol Negotiation)**: Não negociado.

## 4. Verificação do Certificado

A verificação do certificado foi **OK**, mas, como não houve troca de certificados devido à falha na negociação do protocolo, isso não teve impacto prático.

- **Código de retorno da verificação**: `0 (ok)` – Este código indica que, se a negociação tivesse sido bem-sucedida, o certificado teria sido validado corretamente.

## 5. Conclusões

- O erro principal observado é que o servidor **não suporta TLS 1.2**, como indicado pelo código de erro `[SSL: UNSUPPORTED_PROTOCOL]`. Isso ocorre porque o servidor provavelmente foi configurado para suportar apenas **TLS 1.3**.
- A negociação da **cifra** e da **sessão SSL** falhou, e **nenhuma cifra** foi negociada devido ao erro de protocolo.
- **Renegociação segura** não está habilitada no servidor, o que significa que a sessão não poderia ser renegociada de forma segura.
- A verificação de **certificados** foi concluída com sucesso, mas como a negociação foi interrompida, isso não foi efetivamente utilizado.

Este teste mostra que o servidor não está configurado para aceitar conexões com **TLS 1.2** e pode ser necessário atualizar a configuração do servidor para permitir suporte a versões anteriores do protocolo (se desejado), ou remover totalmente o suporte para versões antigas, como **TLS 1.2**.

## Verificação de Chave Privada com OpenSSL

O comando abaixo foi utilizado para verificar a chave privada do servidor (server.key), garantindo que ela não esteja corrompida e está apta a ser usada em conexões seguras:

```bash
openssl rsa -in server.key -check
```

### Resultado:
O comando solicitou a frase secreta (pass phrase) da chave privada para continuar o processo de verificação:

**Enter pass phrase for server.key:**

A verificação foi realizada com sucesso caso não ocorra nenhum erro após a inserção da senha. Esse teste confirma a integridade da chave privada, garantindo que ela pode ser usada para a criação de certificados e para a configuração de conexões seguras TLS/SSL.

## Verificação de Conexão SSL e Certificado do Servidor

O script `Requisição.py` foi executado para estabelecer uma conexão SSL segura com o servidor e verificar o certificado apresentado durante o handshake. O teste garante que a conexão SSL foi realizada com sucesso e que o certificado do servidor está conforme o esperado.

### Resultado:

Abaixo está o log gerado durante a execução do teste:

INFO:root:Conexão SSL estabelecida com autenticação do servidor! INFO:root:Certificado do servidor: {'subject': ((('countryName', 'BR'),), (('stateOrProvinceName', 'São Paulo'),), (('localityName', 'São Paulo'),), (('organizationName', 'Minha Empresa'),), (('commonName', 'localhost'),)), 'issuer': ((('countryName', 'BR'),), (('stateOrProvinceName', 'São Paulo'),), (('localityName', 'São Paulo'),), (('organizationName', 'Minha Empresa'),), (('commonName', 'localhost'),)), 'version': 3, 'serialNumber': '3BCDD07C23D014454CFBFEB49C090E64377668FE', 'notBefore': 'Feb 16 16:37:57 2025 GMT', 'notAfter': 'Feb 16 16:38:57 2026 GMT', 'subjectAltName': (('DNS', 'localhost'),)} INFO:root:Certificado do servidor corresponde ao esperado! INFO:root:Issuer do certificado: ((('countryName', 'BR'),), (('stateOrProvinceName', 'São Paulo'),), (('localityName', 'São Paulo'),), (('organizationName', 'Minha Empresa'),), (('commonName', 'localhost'),)) INFO:root:Certificado emitido pela organização esperada!


### Descrição do Processo:

1. **Conexão SSL Estabelecida**: O script conseguiu estabelecer uma conexão segura com o servidor utilizando SSL, com autenticação do servidor confirmada.
2. **Detalhes do Certificado**: O certificado do servidor foi analisado, mostrando informações cruciais como:
   - **Emissor**: A organização e local do emissor do certificado.
   - **Assunto**: A entidade para a qual o certificado foi emitido (neste caso, "localhost").
   - **Validade**: O certificado é válido de 16 de fevereiro de 2025 até 16 de fevereiro de 2026.
   - **Assunto Alternativo**: O certificado inclui o nome DNS "localhost".
3. **Verificação do Certificado**: O certificado retornado pelo servidor foi validado e correspondeu às expectativas, confirmando que o servidor está utilizando um certificado válido e adequado para a comunicação segura.

### Resumo:

Este teste assegura que o servidor está configurado corretamente com um certificado válido e que a autenticação do servidor foi bem-sucedida, garantindo a segurança na comunicação via SSL/TLS.

## Conclusão

Este projeto demonstra a implementação de um **servidor e cliente HTTPS seguros**, utilizando o **TLS 1.3** para criptografar a comunicação. O servidor foi configurado para trabalhar com um **certificado autoassinado RSA** e utiliza o **algoritmo SHA-256** para garantir a integridade e autenticidade dos dados transmitidos. Além disso, o servidor e o cliente utilizam **HTTP/2** para melhorar o desempenho da comunicação.

A implementação busca fornecer uma base sólida para a construção de sistemas de comunicação segura, com foco em criptografia, autenticação e performance. O projeto pode ser expandido para incluir autenticação mútua (mTLS), suporte a protocolos mais antigos ou novos, e outras funcionalidades de segurança.

