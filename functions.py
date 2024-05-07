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


    def handle_latviski(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Opcija 1')
        itembtn5 = types.KeyboardButton('Opcija 2')
        backbtn = types.KeyboardButton('Back')
        markup.add(itembtn4, itembtn5, backbtn)
        self.bot.send_message(message.chat.id, "Jūs izvēlējāties latviešu valodu. Tagad izvēlieties opciju:", reply_markup=markup)

    def handle_russian(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Вариант 1')
        itembtn5 = types.KeyboardButton('Вариант 2')
        backbtn = types.KeyboardButton('Back')
        markup.add(itembtn4, itembtn5, backbtn)
        self.bot.send_message(message.chat.id, "Вы выбрали русский язык. Теперь выберите вариант:", reply_markup=markup)

    def handle_back(self, message):
        self.start(message)

    def run(self):
        self.bot.polling()

if __name__ == "__main__":
    bot = sellbot('5817517410:AAGS_WQGW6JGq3itWu4TGM7eek9BmycqZrY')
    bot.bot.message_handler(commands=['start'])(bot.start)
    bot.bot.message_handler(func=lambda message: message.text == 'English')(bot.menu_english)
    bot.bot.message_handler(func=lambda message: message.text == 'Latviski')(bot.handle_latviski)
    bot.bot.message_handler(func=lambda message: message.text == 'Русский')(bot.handle_russian)
    bot.bot.message_handler(func=lambda message: message.text == 'Back')(bot.handle_back)
    bot.run()

