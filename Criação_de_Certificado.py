import os
import logging
import datetime
import secrets
import string
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from dotenv import load_dotenv, set_key

# Carregar variáveis de ambiente
load_dotenv()
ENV_FILE = ".env"

# Gerar senha aleatória segura
def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(32))

SENHA_CERTIFICADO = os.getenv("CERT_PASSWORD")
if not SENHA_CERTIFICADO:
    SENHA_CERTIFICADO = gerar_senha()
    set_key(ENV_FILE, "CERT_PASSWORD", SENHA_CERTIFICADO)

# Configuração de logging
logging.basicConfig(level=logging.INFO)

# Função para gerar chave e certificado autoassinado
def gerar_certificado():
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )
        
        encrypted_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(SENHA_CERTIFICADO.encode())
        )

        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "São Paulo"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "São Paulo"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Minha Empresa"),
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        ])

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

        with open("server.key", "wb") as key_file:
            key_file.write(encrypted_key)

        with open("server.crt", "wb") as cert_file:
            cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))

        logging.info("Certificado e chave gerados com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao gerar certificado: {e}")

if __name__ == "__main__":
    gerar_certificado()