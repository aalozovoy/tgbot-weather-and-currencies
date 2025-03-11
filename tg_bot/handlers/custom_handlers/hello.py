from telebot.types import Message
from loader import bot

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet(message: Message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
