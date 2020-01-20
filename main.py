import config
import ptbot


def reply_msg(text):
    bot.send_message(config.CHAT_ID, 'Привет! Ты написал мне: {}'.format(text))


bot = ptbot.Bot(config.API_KEY)
bot.send_message(config.CHAT_ID, 'Бот запущен')
message_id = bot.wait_for_msg(reply_msg)
