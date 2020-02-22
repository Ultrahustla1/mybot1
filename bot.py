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
    user_info = update.message.text.split()
    planet = user_info[1]
    if len(user_info) == 2:
        date = ephem.now()
    else:
        date = user_info[2]
    user_text = getattr(ephem, planet)(date)
    constellation = ephem.constellation(user_text)
    print(constellation)
    update.message.reply_text(constellation)

def all_planets(bot, update):
    planets = ephem._libastro.builtin_planets()
    for planet in planets:
        print(planet)
        update.message.reply_text(planet)
    
def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", call_planet))
    dp.add_handler(CommandHandler("planets", all_planets))

    mybot.start_polling()
    mybot.idle()


main()

