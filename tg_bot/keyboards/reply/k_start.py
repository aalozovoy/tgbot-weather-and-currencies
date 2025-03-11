from telebot import types



markup_start = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn1 = types.KeyboardButton('/weather')
btn2 = types.KeyboardButton('/conversion')
markup_start.add(btn1, btn2)
