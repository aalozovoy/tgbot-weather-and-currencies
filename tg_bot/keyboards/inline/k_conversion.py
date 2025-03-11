from telebot import types

markup_con = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton('RUB🇷🇺/EUR💶', callback_data='rub/eur')
btn2 = types.InlineKeyboardButton('RUB🇷🇺/USD💵', callback_data='rub/usd')
btn3 = types.InlineKeyboardButton('RUB🇷🇺/GBP💷', callback_data='rub/gbp')
btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
markup_con.add(btn1, btn2, btn3, btn4)