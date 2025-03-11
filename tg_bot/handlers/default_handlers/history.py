from loader import bot
from database.db import get_history


@bot.message_handler(commands=['history'])
def history(message):
    history = get_history(message.from_user.id)
    bot.send_message(message.chat.id, f"История запросов:\n{history}")