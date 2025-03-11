from loader import bot

from tg_bot.handlers.custom_handlers.weather import weather
from tg_bot.handlers.custom_handlers.conversion import conversion
from keyboards.reply.k_start import markup_start


@bot.message_handler(commands=['start'])
def main(message):
    image_path = 'img/img_t.jpg'
    with open(image_path, 'rb') as file:
        bot.send_photo(message.chat.id, file)
        bot.reply_to(message, f'Привет, {message.from_user.full_name}!\n'
                              f'Я бот🤖 - помощник путешественника\n'
                              f'Что я умею:\n'
                              f'Выводить данные о погоде\n'
                              f'Конвертировать валюты\n'
                              f'ДАЛЕЕ БУДЕМ ДОБАВЛЯТЬ!!!', reply_markup=markup_start)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'weather':
        weather(call)
    elif call.data == 'conversion':
        conversion(call)