import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from news_pars import parse_news


from config import token 

bot = Bot(token=token )
dp = Dispatcher(bot)


conn = sqlite3.connect('news.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS news
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, news TEXT)''')
conn.commit()


def split_message(message, max_length=4096):
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать! Используйте команду /news для получения новостей.")


@dp.message_handler(commands='news')
async def send_news(message: types.Message):
    news_list = parse_news()
    
    
    for news in news_list:
        cursor.execute("INSERT INTO news (news) VALUES (?)", (news,))
    conn.commit()

    
    response = "\n\n".join(news_list)
    messages = split_message(response)
    for msg in messages:
        await message.reply(msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
