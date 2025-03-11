import requests
from config_data.config import WEATHER_API_KEY

def api_weather(city):
    api_key = WEATHER_API_KEY
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    return response