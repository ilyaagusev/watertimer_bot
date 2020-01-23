import os
from pytimeparse import parse

import ptbot


API_KEY = os.getenv('TELEGRAM_API_KEY')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def notify_finish():
    bot.send_message(CHAT_ID, 'Время вышло!')


def notify_progress(secs_left, message_id, total_seconds):
    progressbar = render_progressbar(total_seconds, secs_left)
    name = "Осталось {0} секунд\n{1}".format(secs_left, progressbar)
    bot.update_message(CHAT_ID, message_id, name)


def render_progressbar(
    total, iteration, prefix='',
    suffix='', length=30, fill='█', zfill='░',
):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply_msg(text):
    seconds = parse(text)
    message_id = bot.send_message(
        CHAT_ID,
        'Таймер запущен на {} секунд'.format(seconds),
        )
    bot.create_countdown(
        seconds, notify_progress,
        message_id=message_id,
        total_seconds=seconds)
    bot.create_timer(
        seconds, notify_finish)


def launch_bot():
    bot.send_message(CHAT_ID, 'Привет!')
    bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
    bot.reply_on_message(reply_msg)
    bot.run_bot()


if __name__ == '__main__':
    bot = ptbot.Bot(API_KEY)
    launch_bot()
