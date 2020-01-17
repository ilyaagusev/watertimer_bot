import config
import ptbot


def notify(name):
    print('hello, ', name)


bot = ptbot.Bot(config.API_KEY)
bot.create_timer(10, notify, 'Viktor')
