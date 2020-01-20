from pytimeparse import parse
import time

import config
import ptbot


def notify(name):
    bot.send_message(config.CHAT_ID, name)


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


def notify_progress(secs_left, message_id, total_seconds):
    if secs_left > 0:
        progressbar = render_progressbar(total_seconds, secs_left)
        name = "Осталось {0} секунд\n{1}".format(secs_left, progressbar)
        bot.update_message(config.CHAT_ID, message_id, name)
    else:
        bot.update_message(config.CHAT_ID, message_id, 'Время вышло!')


def create_timer(timeout_secs, callback, *arg):
    time.sleep(timeout_secs)
    return callback(*arg)


def reply_msg(text):
    seconds = parse(text)
    message_id = bot.send_message(
        config.CHAT_ID,
        'Таймер запущен на {} секунд'.format(seconds),
        )
    bot.create_countdown(
        seconds, notify_progress,
        message_id=message_id,
        total_seconds=seconds)


bot = ptbot.Bot(config.API_KEY)
bot.send_message(config.CHAT_ID, 'Привет!')
bot.send_message(config.CHAT_ID, 'На сколько запустить таймер?')
bot.wait_for_msg(reply_msg)
