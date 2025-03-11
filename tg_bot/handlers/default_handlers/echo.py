from loader import bot
from keyboards.reply.k_start import markup_start


@bot.message_handler(state=None)
def bot_echo(message):
    bot.reply_to(message, 'Выберите действие\n'
                          '/help - Помощь\n'
                          '/history - История запросов\n'
                          '/weather - Узнать погоду\n'
                          '/conversion - Конвертация валют', reply_markup=markup_start)










