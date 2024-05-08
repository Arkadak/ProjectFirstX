import aiogram
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
        self.bot.send_message(message.chat.id,"Select Language", reply_markup=markup)

    def menu_english(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        menup = types.KeyboardButton('Pizza')
        menus = types.KeyboardButton('Sushi')
        backbtn = types.KeyboardButton('Back')
        markup.add(menup, menus, backbtn)
        self.bot.send_message(message.chat.id, "You selected English. Now choose a meal:", reply_markup=markup)


    def menu_latviski(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Pizza')
        itembtn5 = types.KeyboardButton('Suši')
        backbtn = types.KeyboardButton('Majas')
        markup.add(itembtn4, itembtn5, backbtn)
        self.bot.send_message(message.chat.id, "Jūs izvēlējāties latviešu valodu. Tagad izvēlieties edienu:", reply_markup=markup)

    def menu_russian(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Пицца')
        itembtn5 = types.KeyboardButton('Суши')
        backbtn = types.KeyboardButton('Домой')
        markup.add(itembtn4, itembtn5, backbtn)
        self.bot.send_message(message.chat.id, "Вы выбрали русский язык. Теперь выберите еду:", reply_markup=markup)

    def menu_back(self, message):
        self.start(message)

    def run(self):
        self.bot.polling()

if __name__ == "__main__":
    bot = sellbot('5817517410:AAGS_WQGW6JGq3itWu4TGM7eek9BmycqZrY')
    bot.bot.message_handler(commands=['start'])(bot.start)
    bot.bot.message_handler(func=lambda message: message.text == 'English')(bot.menu_english)
    bot.bot.message_handler(func=lambda message: message.text == 'Latviski')(bot.menu_latviski)
    bot.bot.message_handler(func=lambda message: message.text == 'Русский')(bot.menu_russian)
    bot.bot.message_handler(func=lambda message: message.text == 'Back')(bot.menu_back)
    bot.bot.message_handler(func=lambda message: message.text == 'Majas')(bot.menu_back)
    bot.bot.message_handler(func=lambda message: message.text == 'Домой')(bot.menu_back)
    bot.run()
