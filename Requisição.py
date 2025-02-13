import requests

try:
    response = requests.get("https://localhost:4443", verify="./server.crt")
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
