from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import datetime

# Gerar chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Criar detalhes do certificado
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "São Paulo"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "São Paulo"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Minha Empresa"),
    x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
])

# Criar certificado
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName("localhost")]),  # Adicionar SAN
        critical=False,
    )
    .sign(private_key, hashes.SHA256())
)

# Salvar chave privada
with open("server.key", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

# Salvar certificado
with open("server.crt", "wb") as cert_file:
    cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

print("Certificado e chave gerados com sucesso!")
