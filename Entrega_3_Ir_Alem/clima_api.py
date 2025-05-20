
import requests

API_KEY = "sua_api_key_aqui"  # Substitua pela sua chave da OpenWeather
CIDADE = "São Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    dados = response.json()
    temp = dados['main']['temp']
    clima = dados['weather'][0]['description']
    previsao_chuva = any('rain' in w['main'].lower() for w in dados['weather'])

    print(f"Temperatura atual: {temp}°C")
    print(f"Clima: {clima}")
    if previsao_chuva:
        print("Previsão de chuva detectada. Irrigação DESLIGADA.")
    else:
        print("Sem previsão de chuva. Irrigação pode ser ATIVADA.")
else:
    print("Erro ao obter dados da API.")
