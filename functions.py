import telebot
from telebot import types

class sellbot:
    def __init__(self,token):
        self.bot = telebot.TeleBot(token)

    def start(self,message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton("English")
        itembtn2 = types.KeyboardButton("Latviski")
        itembtn3 = types.KeyboardButton("Русский")
        markup.add(itembtn1, itembtn2, itembtn3)
        self.bot.send_message(message.chat.id, "Choose one option:", reply_markup=markup)

    def run(self):
        self.bot.polling()

if __name__ == "__main__":
    bot = sellbot('5817517410:AAGS_WQGW6JGq3itWu4TGM7eek9BmycqZrY')
    bot.bot.message_handler(commands=['start'])(bot.start)
    bot.run()

