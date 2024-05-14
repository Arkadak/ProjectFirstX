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

    async def menu(self,message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        car = types.KeyboardButton("Cars")
        food = types.KeyboardButton("Food")
        backbtn = types.KeyboardButton('Back')
        markup.add(car, food,backbtn)
        await message.answer("Select category", reply_markup=markup)
    async def menul(self,message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        car = types.KeyboardButton("Mašinas")
        food = types.KeyboardButton("Ēdiens")
        backbtn = types.KeyboardButton('Majas')
        markup.add(car, food, backbtn)
        await message.answer("Izvelejaties sadaļu", reply_markup=markup)
    async def menur(self,message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        car = types.KeyboardButton("Машины")
        food = types.KeyboardButton("Еда")
        backbtn = types.KeyboardButton('Домой')
        markup.add(car, food, backbtn)
        await message.answer("Выберите раздел", reply_markup=markup)

    async def cars(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton("Porsche 911 Turbo S")
        itembtn2 = types.KeyboardButton("Volvo V90")
        itembtn3 = types.KeyboardButton("Porsche 718")
        itembtn4 = types.KeyboardButton("Lancia Delta")
        backbtn = types.KeyboardButton('Back')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, backbtn)
        await message.answer("Select Language", reply_markup=markup)
    async def carsl(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton("Porsche 911 Turbo S")
        itembtn2 = types.KeyboardButton("Volvo V90")
        itembtn3 = types.KeyboardButton("Porsche 718")
        itembtn4 = types.KeyboardButton("Lancia Delta")
        backbtn = types.KeyboardButton('Majas')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, backbtn)
        await message.answer("Select Language", reply_markup=markup)
    async def carsr(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton("Porsche 911 Turbo S")
        itembtn2 = types.KeyboardButton("Volvo V90")
        itembtn3 = types.KeyboardButton("Porsche 718")
        itembtn4 = types.KeyboardButton("Lancia Delta")
        backbtn = types.KeyboardButton('Домой')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, backbtn)
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
        url_pizza = "https://www.lulu.lv/picas/super-lulu-pica"
        urlf_pizza = "https://www.lulu.lv/cache/images/1856548973/super-lulu-pica_1675938940.jpg"
        await bot.send_invoice(message.chat.id, "buy", "Pizza", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Super Lulu", 25*100)], photo_url=urlf_pizza, photo_width=100, photo_height=75)
        await bot.send_message(message.chat.id, url_pizza)
    async def buy_sushi(self, message: types.Message):
        url_sushi = "https://www.ganbei.lv/sushi.75.pg"
        urlf_sushi = "https://www.ganbei.lv/49h1-gan-bei-futomaki-12-gab-.16817-15.jpeg"
        await bot.send_invoice(message.chat.id, "buy", "Sushi", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Futomaki", 29*100)], photo_url=urlf_sushi, photo_width=100, photo_height=56)
        await bot.send_message(message.chat.id, url_sushi)

    async def buy_911(self, message: types.Message):
        url_911 = "https://www.ss.lv/msg/lv/transport/cars/porsche/911/cbpodi.html"
        urlf_911 ="https://i.ss.lv/gallery/7/1218/304455/porsche-911-2-60890919.800.jpg"
        await bot.send_invoice(message.chat.id, "buy", "Porsche", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("992", 229 * 100)], photo_url=urlf_911, photo_width=100, photo_height=75)
        await bot.send_message(message.chat.id, url_911)
    async def buy_718(self, message: types.Message):
        url_718 = "https://www.ss.lv/msg/lv/transport/cars/porsche/cayman/ccecfg.html"
        urlf_718 = "https://i.ss.com/gallery/6/1128/281840/porsche-cayman-2-56367824.800.jpg"
        await bot.send_invoice(message.chat.id, "buy", "Porsche", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Cayman", 77*100)], photo_url=urlf_718, photo_width=100, photo_height=75)
        await bot.send_message(message.chat.id, url_718)
    async def buy_V90(self, message: types.Message):
        url_V90 = "https://www.ss.lv/msg/lv/transport/cars/volvo/v90/cbxnge.html"
        urlf_V90 = "https://i.ss.lv/gallery/6/1171/292685/volvo-v90-1-58536921.800.jpg"
        await bot.send_invoice(message.chat.id, "buy", "Volvo", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("V90", 54*100,)], photo_url=urlf_V90, photo_width=100, photo_height=75)
        await bot.send_message(message.chat.id, url_V90)
    async def buy_Delta(self, message: types.Message):
        url_Delta = "https://www.ss.lv/msg/lv/transport/cars/lancia/delta/ffngb.html#photo-15"
        urlf_Delta = "https://i.ss.lv/gallery/7/1204/300756/lancia-delta-2-60151022.800.jpg"
        await bot.send_invoice(message.chat.id, "buy", "Lancia", "invoice", tokens.PAYMENT_TOKEN, "EUR", [types.LabeledPrice("Delta", 5550*100)], photo_url=urlf_Delta, photo_width=100, photo_height=75)
        await bot.send_message(message.chat.id, url_Delta)



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
    await sellbot.menu(message)


@dp.message_handler(lambda message: message.text == 'Latviski')
async def handle_latviski(message: types.Message):
    await sellbot.menul(message)


@dp.message_handler(lambda message: message.text == 'Русский')
async def handle_russian(message: types.Message):
    await sellbot.menur(message)


@dp.message_handler(lambda message: message.text == 'Домой' or message.text == "Back" or message.text == "Majas")
async def menu_back(message: types.Message):
    await sellbot.menu_back(message)

@dp.message_handler(lambda message: message.text =='Pizza' or message.text == "Пицца")
async def buy_pizza(message: types.Message):
    await sellbot.buy_pizza(message)

@dp.message_handler(lambda message: message.text == 'Суши' or message.text == "Sushi" or message.text =="Suši")
async def buy_sushi(message: types.Message):
    await sellbot.buy_sushi(message)

@dp.message_handler(lambda message: message.text == 'Cars')
async def cars(message: types.Message):
    await sellbot.cars(message)

@dp.message_handler(lambda message: message.text == 'Машины')
async def carsr(message: types.Message):
    await sellbot.carsr(message)

@dp.message_handler(lambda message: message.text == 'Mašinas')
async def carsl(message: types.Message):
    await sellbot.carsl(message)

@dp.message_handler(lambda message: message.text == 'Food')
async def menu_english(message: types.Message):
    await sellbot.menu_english(message)

@dp.message_handler(lambda message: message.text == 'Ēdiens')
async def menu_latviski(message: types.Message):
    await sellbot.menu_latviski(message)

@dp.message_handler(lambda message: message.text == 'Еда')
async def menu_russian(message: types.Message):
    await sellbot.menu_russian(message)

@dp.message_handler(lambda message: message.text == 'Porsche 911 Turbo S')
async def buy_911(message: types.Message):
    await sellbot.buy_911(message)
@dp.message_handler(lambda message: message.text == 'Porsche 718')
async def buy_718(message: types.Message):
    await sellbot.buy_718(message)
@dp.message_handler(lambda message: message.text == 'Volvo V90')
async def buy_V90(message: types.Message):
    await sellbot.buy_V90(message)
@dp.message_handler(lambda message: message.text == 'Lancia Delta')
async def buy_Delta(message: types.Message):
    await sellbot.buy_Delta(message)

sellbot.run()
