import logging, ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from api_key import API_KEY

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def call_planet(bot, update):
    date = update.message.text.split()
    date = date[1]
    user_text = ephem.Planet(date)
    constellation = ephem.constellation(user_text)
    print(constellation)
    update.message.reply_text(constellation)
    
def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", call_planet))

    mybot.start_polling()
    mybot.idle()


main()

