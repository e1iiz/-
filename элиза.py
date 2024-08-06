# import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from news_pars import parse_news
from hw5_smtp import send_news  
from aiogram.types import BotCommand
from logging import basicConfig, INFO
from config import token 

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

def split_message(message, max_length=4096):
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply(f"Добро пожаловать, {message.from_user.full_name}! Если хотите узнать об новостях, введите команду /news")

@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    news_list = parse_news()

    response = "\n\n".join(news_list)
    messages = split_message(response)
    for msg in messages:
        await message.reply(msg)
    # await message.answer(' /send для того чтобы отправить новости другу через почту')

@dp.message_handler(commands='send')
async def send_email(message: types.Message):
    
    recipient_email = "elizaerkinbekova@gmail.com"

    try:
        send_news(recipient_email, parse_news())
        await message.answer("Новости успешно отправлены на email!")
    except Exception as e:
        await message.answer(f"Не удалось отправить новости: {e}")

async def on_startup(dp):
    await bot.set_my_commands([
        BotCommand(command='/start',description= ' Запустит бот'),
        BotCommand(command='/news',description='новости'),
        BotCommand(command='/send',description='отправить новостей через почту')
    ])

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup, skip_updates=True)
