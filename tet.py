from aiogram import Bot, Dispatcher, executor, types
import tokens

bot = Bot(tokens.BOT_TOKEN)
dp = Dispatcher(bot)

class tet:
    def __init__(self, bot):
        self.bot = bot

    async def start(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(row_width=2)

        markup.add()
        await message.answer("Sveicinati tet veikala", reply_markup=markup)