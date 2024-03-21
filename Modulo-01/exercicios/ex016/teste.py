
import requests

# Sua chave de API do Google Maps
api_key = "AIzaSyAQBZOAZGzqv4nqNVj0AKX5rnWq-JcavM0"

# Sua lista de endereços
addresses = ["Rua 1, Bairro 1, Cidade 1", "Rua 2, Bairro 2, Cidade 2", "Rua 3, Bairro 3, Cidade 3", "Rua 4, Bairro 4, Cidade 4", "Rua 5, Bairro 5, Cidade 5", "Rua 6, Bairro 6, Cidade 6", "Rua 7, Bairro 7, Cidade 7", "Rua 8, Bairro 8, Cidade 8", "Rua 9, Bairro 9, Cidade 9", "Rua 10, Bairro 10, Cidade 10"]

# O endereço de destino
destination = "Rua Principal, Bairro Principal, Cidade Principal"

# Inicializar variáveis para armazenar a distância mínima e o endereço mais próximo
min_distance = float("inf")
closest_address = ""

# Loop através de cada endereço
for address in addresses:
    # Construir a URL de solicitação
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={address}&destinations={destination}&key={api_key}"
    
    # Enviar a solicitação e armazenar a resposta
    response = requests.get(url).json()
    
    # Obter a distância entre o endereço atual e o destino
    distance = response["rows"][0]["elements"][0]["distance"]["value"]
    
    # Se a distância for menor do que a distância mínima atual, atualize a distância mínima e o endereço mais próximo
    if distance < min_distance:
        min_distance = distance
        closest_address = address

# Imprima o endereço mais próximo
print(f"O endereço mais próximo é: {closest_address}")