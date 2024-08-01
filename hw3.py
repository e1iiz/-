from aiogram  import Bot, Dispatcher,types,executor
from config import token
import random
import logging
from aiogram.types import BotCommand

bot = Bot(token=token)
dp = Dispatcher(bot)

quotes=['Что разум человека может постигнуть и во что он может поверить, того он способен достичь',
        'Стремитесь не к успеху, а к ценностям, которые он дает',
        'Сложнее всего начать действовать, все остальное зависит только от упорства.',
        'Надо любить жизнь больше, чем смысл жизни',
        'Жизнь - это то, что с тобой происходит, пока ты строишь планы.']

# random_quotes=random.choice(quotes)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Введите команду /quote , чтобы получить случайные цитаты.")

@dp.message_handler(commands='quote')
async def quote(message: types.Message):
    random_quotes=random.choice(quotes)
    await message.answer(random_quotes)

executor.start_polling(dp)
