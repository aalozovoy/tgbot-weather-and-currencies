import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
DEFAULT_COMMANDS = (
    ('help', 'Помощь'),
    ('start', 'Запуск бота'),
    ('weather', 'Узнать погоду'),
    ('conversion', 'Конвертация валют'),
    ('history', 'История запросов'),
)
