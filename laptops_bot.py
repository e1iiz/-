from aiogram import Bot,Dispatcher,types,executor
from  aiogram.types import LabeledPrice,PreCheckoutQuery,CallbackQuery,BotCommand
from aiogram.utils.callback_data import CallbackData
from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup
from config import token,pay_token
import logging

bot=Bot(token=token)
dp=Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

buy_laptop=CallbackData('buy','item_id')

start_buttons=[
    types.KeyboardButton('товары'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Контакты')
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='Адрес')
async def send_adress(message:types.Message):
    await message.reply("Наш адрес: Город Ош, 194-224 Курманжан-Датка ул ")    
    await message.reply_location(40.521534, 72.799456)

@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.answer(f'{message.from_user.full_name}, вот нащи контакты: ')
    await message.answer_contact("+996777797921", "Eliza", "Erkinbek kyzy")

@dp.message_handler(text='товары')
async def tovar(message:types.Message):
    keyboard=InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Ноутбук HP VICTUS', callback_data=buy_laptop.new(item_id = 'laptop')))
    keyboard.add(InlineKeyboardButton(text='Ноутбук ASUS', callback_data=buy_laptop.new(item_id = 'laptop 1')))
    keyboard.add(InlineKeyboardButton(text='Ноутбук Dell', callback_data=buy_laptop.new(item_id = 'laptop 2')))
    keyboard.add(InlineKeyboardButton(text='Ноутбук Acer Aspire', callback_data=buy_laptop.new(item_id = 'laptop 3')))
    keyboard.add(InlineKeyboardButton(text='Ноутбук Dell Vostro', callback_data=buy_laptop.new(item_id = 'laptop 4')))
    await message.answer("Привет выбери товар для покупки", reply_markup=keyboard)

@dp.callback_query_handler(buy_laptop.filter(item_id = 'laptop'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label='HP Victus', amount=7000000)]


    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop',
        description='Ноутбук HP VICTUS 15-fa0031dx Intel Core i5-12450H(3.30-4.40GHz),8GB DDR4,512GB SSD m.2 NVMe,NVIDIA GTX 1650 4GB GDDR6,15.6" FHD(1920x1080)144Hz IPS,WiFi ac,BT 5.0,HD WC,CR,Win11,MicaSilv[68U87UA#ABA]',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/abb/1000_1000_1d0e97ea46f4438969ab06dd5b311ca67/abb3c7028d30f6d965fa949510ad6426.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Характеристика', callback_data='characteristic'))
    await bot.send_message(chat_id=callback.from_user.id, text="Хотите узнать характеристику?", reply_markup=keyboard)
    
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == 'characteristic')
async def show_characteristic(callback: CallbackQuery):
    await callback.message.answer("Характеристика ноутбука: \n- Intel Core i5-12450H\n- 8GB DDR4\n- 512GB SSD m.2 NVMe\n- NVIDIA GTX 1650 4GB GDDR6\n- 15.6\" FHD 144Hz IPS")
    await callback.answer()
    

@dp.callback_query_handler(buy_laptop.filter(item_id = 'laptop 1'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label='ASUS', amount=4773000)]
    
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop 1',
        description='Ноутбук ASUS X1502ZA-EJ1426 Intel Core i5-12500H (up to 4.5Ghz), 8GB DDR4, 512GB M.2 NVMe™ PCIe® 3.0 SSD, Int VGA, 15.6"FULL HD (1920x1080), WiFi 6, BT 5.0, HD WebCam, DOS, Silver',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/789/800_800_1d0e97ea46f4438969ab06dd5b311ca67/789859dfa6d1874759b6d30832460f50.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Характеристика', callback_data='characteristic 1'))
    await bot.send_message(chat_id=callback.from_user.id, text="Хотите узнать характеристику?", reply_markup=keyboard)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == 'characteristic 1')
async def show_characteristic(callback: CallbackQuery):
    await callback.message.answer(f"""  Bluetooth:	Да\n	
    Web-камера:	Да\n	
    WIFI: Да\n	
    Диагональ:	15.6\n	
    Объём накопителя ГБ: 512\n	
    Объём оперативной памяти, ГБ:	8\n
    Операционная система:	DOS\n
    Процессор:	Intel Core i5-12500H\n	
    Разрешение экрана:	1920 x 1280\n
    Тип жесткого диска:	SSD\n	
    Цвет:	Серебристый\n
    Чипсет видеоадаптера:	Int VGA""")
    await callback.answer()

@dp.callback_query_handler(buy_laptop.filter(item_id = 'laptop 2'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label=' Dell', amount=9726600)]
    
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop 2',
        description='Ноутбук Dell Inspiron 16 Plus 7620 Intel Core i7-12700H (up to 4.7GHz), 16GB DDR5, 1 TB NVMe, 16"FHD 3K (3072x1920) RTX 3050 4GB, WF6, скан. отп. пальц., Win11 PRO,подсветка, Eng-Rus, темно зеленый',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/4c8/800_800_1d0e97ea46f4438969ab06dd5b311ca67/4c88dd391c5556c85adcbea698ea3c03.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Характеристика', callback_data='characteristic 2'))
    await bot.send_message(chat_id=callback.from_user.id, text="Хотите узнать характеристику?", reply_markup=keyboard)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == 'characteristic 2')
async def show_characteristic(callback: CallbackQuery):
    await callback.message.answer(f"""  Bluetooth:	Да\n	
    Web-камера:	Да\n	
    WIFI:	Да\n	
    Диагональ:	17.3\n	
    Объём накопителя ГБ:	1 TB\n	
    Объём оперативной памяти, ГБ:	16\n	
    Объём памяти видеоадаптера Мб:	4096\n	
    Операционная система:	Windows 11 Pro\n
    Процессор:	Intel Core i7-12700H\n	
    Разрешение экрана:	3072x1920\n	
    Тип жесткого диска:	SSD\n	
    Чипсет видеоадаптера:	NVIDIA® GeForce® RTX 3050""")
    await callback.answer()

@dp.callback_query_handler(buy_laptop.filter(item_id = 'laptop 3'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label='Acer Aspire', amount=3921600)]
    
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop 3',
        description='Ноутбук Acer Aspire 3 Intel i3-1215U (3.30-4.40Ghz), 12GB DDR4, 2TB PCIe NVMe SSD, 15.6" FHD TN, WiFi, LAN, Bluetooth, DOS, Eng-Rus, серебро [NX.K6TEM.004]',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/e3a/300_300_1/e3a52f8232d2299be78c820c144aa672.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Характеристика', callback_data='characteristic 3'))
    await bot.send_message(chat_id=callback.from_user.id, text="Хотите узнать характеристику?", reply_markup=keyboard)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == 'characteristic 3')
async def show_characteristic(callback: CallbackQuery):
    await callback.message.answer(f"""  Bluetooth:	Да\n	
    Web-камера:	Да\n	
    WIFI:	Да\n	
    Диагональ:	15.6\n	
    Объём накопителя ГБ:	1 TB\n	
    Объём оперативной памяти, ГБ:	12\n	
    Операционная система:	DOS\n
    Процессор:	Intel Core i3-1215U\n	
    Разрешение экрана:	1920x1080FHD\n	
    Тип жесткого диска:	SSD\n	
    Чипсет видеоадаптера:	интегрированная""")
    await callback.answer()

@dp.callback_query_handler(buy_laptop.filter(item_id = 'laptop 4'))
async def process_payment(callback:CallbackQuery):
    price = [LabeledPrice(label=' Dell Vostro', amount=4360200)]
    
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop 4',
        description='Ноутбук Dell Vostro 3520 Intel Core i3-1215U (3.30-4.40Ghz), 32GB, 2TB PCIe NVMe SSD, 15.6" FHD IPS 120hz, WiFi, Bluetooth, LAN RJ45, DOS, Eng-Rus, черный',
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/656/800_800_1d0e97ea46f4438969ab06dd5b311ca67/656da209acaeda58436150d34c81b2c0.jpg',
        photo_height=512,
        photo_size=512,
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text='Характеристика', callback_data='characteristic 4'))
    await bot.send_message(chat_id=callback.from_user.id, text="Хотите узнать характеристику?", reply_markup=keyboard)
    
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == 'characteristic 4')
async def show_characteristic(callback: CallbackQuery):
    await callback.message.answer(f"""  Bluetooth:	Да\n	
    Web-камера:	Да\n	
    WIFI:	Да\n	
    Диагональ:	15.6\n	
    Объём накопителя ГБ:	2TB+1TB\n	
    Объём оперативной памяти, ГБ:	32\n	
    Операционная система:	DOS\n
    Процессор:	Intel Core i3-1215U\n	
    Разрешение экрана:	1920x1080FHD\n	
    Тип жесткого диска:	SSD\n
    Цвет:	Черный\n	
    Чипсет видеоадаптера:	интегрированная""")
    await callback.answer()

    
@dp.pre_checkout_query_handler(lambda query : True)
async def pre(pre: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre.id, ok=True)
    
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def suc(message: types.Message):
    await message.reply("Спасибо за покупку")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  