import config
import ptbot
import time


def notify(name):
    bot.send_message(config.CHAT_ID, name) 


def create_timer(timeout_secs, callback, callback_arg):
    time.sleep(timeout_secs)
    return callback(callback_arg)


bot = ptbot.Bot(config.API_KEY)
create_timer(10, notify, 'Время вышло!')
