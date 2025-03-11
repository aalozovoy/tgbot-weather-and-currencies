from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from database.db import init_db

if __name__ == "__main__":
    set_default_commands(bot)
    init_db()
    bot.infinity_polling()
