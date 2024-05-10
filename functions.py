from aiogram import Bot, Dispatcher, executor, types
import tokens

bot = Bot(tokens.BOT_TOKEN)
dp = Dispatcher(bot)


class Sellbot:
    def __init__(self, bot):
        self.bot = bot

    async def start(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton("English")
        itembtn2 = types.KeyboardButton("Latviski")
        itembtn3 = types.KeyboardButton("Русский")
        markup.add(itembtn1, itembtn2, itembtn3)
        await message.answer("Select Language", reply_markup=markup)

    async def menu_english(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        menup = types.KeyboardButton('Pizza')
        menus = types.KeyboardButton('Sushi')
        backbtn = types.KeyboardButton('Back')
        markup.add(menup, menus, backbtn)
        await message.answer("You selected English. Now choose a meal:", reply_markup=markup)

    async def menu_latviski(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Pizza')
        itembtn5 = types.KeyboardButton('Suši')
        backbtn = types.KeyboardButton('Majas')
        markup.add(itembtn4, itembtn5, backbtn)
        await message.answer("Jūs izvēlējāties latviešu valodu. Tagad izvēlieties edienu:", reply_markup=markup)

    async def menu_russian(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn4 = types.KeyboardButton('Пицца')
        itembtn5 = types.KeyboardButton('Суши')
        backbtn = types.KeyboardButton('Домой')
        markup.add(itembtn4, itembtn5, backbtn)
        await message.answer("Вы выбрали русский язык. Теперь выберите еду:", reply_markup=markup)
    async def buy_pizza(self, message: types.Message):
        await bot.send_invoice(message.chat.id, "buy","Pizza", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Pizza", 11*100)])

    async def buy_sushi(self, message: types.Message):
        await bot.send_invoice(message.chat.id, "buy","Sushi", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Pizza", 5*100)])


    async def menu_back(self, message: types.Message):
        await self.start(message)

    def run(self):
        executor.start_polling(dp)
        bot.run()


sellbot = Sellbot(bot)

@dp.message_handler(lambda message: message.text == '/start')
async def start(message: types.Message):
    await sellbot.start(message)


@dp.message_handler(lambda message: message.text == 'English')
async def handle_english(message: types.Message):
    await sellbot.menu_english(message)


@dp.message_handler(lambda message: message.text == 'Latviski')
async def handle_latviski(message: types.Message):
    await sellbot.menu_latviski(message)


@dp.message_handler(lambda message: message.text == 'Русский')
async def handle_russian(message: types.Message):
    await sellbot.menu_russian(message)


@dp.message_handler(lambda message: message.text == 'Домой' or message.text == "Back" or message.text == "Majas")
async def menu_back(message: types.Message):
    await sellbot.menu_back(message)

@dp.message_handler(lambda message: message.text =='Pizza' or message.text == "Пицца")
async def buy_pizza(message: types.Message):
    await sellbot.buy_pizza(message)

@dp.message_handler(lambda message: message.text == 'Суши' or message.text == "Sushi" or message.text =="Suši")
async def buy_sushi(message: types.Message):
    await sellbot.buy_sushi(message)

sellbot.run()
