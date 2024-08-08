import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO
import aioschedule
import time

# Configure logging
basicConfig(level=INFO)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)

def get_laptops():
    url = 'https://www.sulpak.kg/f/noutbuki'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    product_containers = soup.select('.product__item-inner')
    if not product_containers:
        print("No products found. Check the selectors.")
        return laptops

    for item in product_containers:
        title_element = item.select_one('.product__item-name a')
        price_element = item.select_one('.product__item-price')
        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True).replace('сом', '').strip()
            laptops.append({
                'title': title,
                'price': price
            })

    return laptops

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.full_name}!')

@dp.message_handler(commands='laptop')
async def laptop(message: types.Message):
    laptops = get_laptops()
    if not laptops:
        await message.reply('Не получилось получить данные о ноутбуках.')
    for laptop in laptops:
        await message.reply(f"{laptop['title']}\nЦена: {laptop['price']} сом")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
