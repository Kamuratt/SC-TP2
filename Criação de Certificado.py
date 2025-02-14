import string
import secrets
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import datetime

# Senha fixa e segura para a criptografia da chave privada
senha_gerada = "VxG$7t@4pL8M1jR#f3D9&zQzK$LwQ@t2"

# Função para gerar chave e certificado
def gerar_certificado():
    global senha_gerada  # Declara a variável como global

    try:
        # Gerar chave privada RSA de 4096 bits
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )

        # Criptografar a chave privada com a senha gerada
        encrypted_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(senha_gerada.encode())
        )

        # Definir sujeito e emissor (certificado autoassinado)
        subject = issuer = x509.Name([ 
            x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "São Paulo"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "São Paulo"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Minha Empresa"),
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        ])

        # Gerar certificado autoassinado com validade de 1 ano
        certificate = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(private_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow() - datetime.timedelta(minutes=1))
            .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
            .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
            .add_extension(
                x509.SubjectAlternativeName([x509.DNSName("localhost")]),
                critical=False,
            )
            .sign(private_key, hashes.SHA256())
        )

        # Definir nomes para os arquivos de chave e certificado
        chave_filename = "server.key"
        cert_filename = "server.crt"

        # Salvar a chave privada criptografada
        with open(chave_filename, "wb") as key_file:
            key_file.write(encrypted_key)

        # Salvar o certificado
        with open(cert_filename, "wb") as cert_file:
            cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))

        print(f"Certificado e chave gerados com sucesso! A senha gerada foi: {senha_gerada}")
        print(f"Chave salva em: {chave_filename}")
        print(f"Certificado salvo em: {cert_filename}")

    except Exception as e:
        print(f"Erro ao gerar certificado e chave: {e}")

# Chamar a função para gerar o certificado e chave
gerar_certificado()
