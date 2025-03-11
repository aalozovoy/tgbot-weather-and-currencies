from loader import bot
from currency_converter import CurrencyConverter # библиотека для конвертации валют
from keyboards.inline.k_conversion import markup_con


currency = CurrencyConverter()
class UserState:
    def __init__(self):
        self.amount = 0
user_states = {}

@bot.message_handler(commands=['conversion'])
def conversion(message):
    # log_request(message.from_user.id, 'conversion')
    image_path = 'img/img_c.jpg'
    with open(image_path, 'rb') as file:
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, '<b>Введите сумму</b>', parse_mode='html')
        bot.register_next_step_handler(message, summa)


def summa(message):
    user_id = message.from_user.id
    user_state = user_states.setdefault(user_id, UserState())

    try:
        user_state.amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Введено не корректное значение суммы! Повторите ввод!')
        bot.register_next_step_handler(message, summa)
        return
    if user_state.amount > 0:
        bot.send_message(message.chat.id, 'Выберите пару валют.', reply_markup=markup_con)
    else:
        bot.send_message(message.chat.id, 'Вы ввели отрицательное значение! Повторите ввод!')
        bot.register_next_step_handler(message, summa)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_id = call.from_user.id
    user_state = user_states.get(user_id)
    if call.data != 'else':
        val = call.data.upper().split('/')
        res = currency.convert(user_state.amount, val[0], val[1])
        bot.send_message(call.message.chat.id, f'{user_state.amount} {val[0]} = {round(res, 3)} {val[1]}')

    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш (usd/eur)')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    user_id = message.from_user.id
    user_state = user_states.get(user_id)
    try:
        val = message.text.upper().split('/')
        res = currency.convert(user_state.amount, val[0], val[1])
        bot.send_message(message.chat.id, f'{user_state.amount} {val[0]} = {round(res, 3)} {val[1]}')
    except Exception:
        bot.send_message(message.chat.id, 'Введено не корректное значение суммы! Повторите ввод!')
        bot.register_next_step_handler(message, my_currency)
