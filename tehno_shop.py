from aiogram import Bot, Dispatcher, types, executor
from config import token 
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('о нас'),
    types.KeyboardButton('товары'),
    types.KeyboardButton('заказать'),
    types.KeyboardButton('контакты')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='о нас')
async def about_us(message: types.Message):
    await message.reply('TechnoShop - это интернет-магазин смартфонов. У нас есть:')
    await message.answer('Большой выбор товаров')
    await message.answer('Бесплатная доставка')
    await message.answer('Характеристики')
    await message.answer('Скидки и акции')

@dp.message_handler(text="контакты")
async def contact(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, вот наши контакты: ')
    await message.answer_contact("+996777797921", "Eliza", "Erkinbek kyzy")
    await message.answer_contact("+996990130081", "Нуриза", "Jolboldieva")

kinds_s = [
    types.KeyboardButton('Xiaomi'),
    types.KeyboardButton('iPhone'),
    types.KeyboardButton('Huawei'),
    types.KeyboardButton("Назад")
]

kinds_s_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*kinds_s)

@dp.message_handler(text='товары')
async def pro(message: types.Message):
    await message.answer("Какой смартфон вы хотите", reply_markup=kinds_s_keyboard)

mi = [
    types.KeyboardButton('Xiaomi Mi A2 Lite 3'),
    types.KeyboardButton('Xiaomi Mi 8 Lite'),
    types.KeyboardButton('Xiaomi Redmi 6'),
    types.KeyboardButton('Xiaomi Redmi Note 6 Pro(black)'),
    types.KeyboardButton("Назад")
]

mi_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*mi)

@dp.message_handler(text='Xiaomi')
async def kind_xiami(message: types.Message):
    await message.answer("Выбираете", reply_markup=mi_keyboard)

@dp.message_handler(text='Xiaomi Mi A2 Lite 3')
async def front1(message: types.Message):
    await message.reply("""https://i0.wp.com/techshop.kg/wp-content/uploads/2018/09/ritm025.jpg?resize=300%2C300&ssl=1""")
    await message.reply("Смартфон Xiaomi Mi A2 Lite 4")
    await message.reply("11,400 сом ")
    await message.answer(f"\nХарактеристики\nСмартфон на платформе Android\nПоддержка двух SIM-карт\nЭкран 5.84″, разрешение 2280×1080\nДвойная камера 12/5 МП, автофокус, F/2.2\nПамять 32 Гб\nСлот для карты памяти\n3G, 4G LTE, Wi-Fi, Bluetooth, GPS,\nОбъем оперативной памяти 3 Гб\nАккумулятор 4000 мА⋅ч\nВес 178 г")

@dp.message_handler(text='Xiaomi Mi 8 Lite')
async def front2(message: types.Message):
    await message.reply("""https://i1.wp.com/techshop.kg/wp-content/uploads/2018/12/xiaomi-mi-8-lite-black.jpg?resize=150%2C150&ssl=1""")   
    await message.reply("Xiaomi Mi 8 Lite 64 Gb (RAM 4 Gb) Dual Sim blue")
    await message.reply("15,970 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА  \nОперационная система телефона: Android\nСерия телефона: Mi 8 Lite\nВерсия ОС телефона : Android 8.1\nКоличество SIM-карт телефона: 2\nТип корпуса телефона: моноблок\nУправление телефоном: сенсорные кнопки\nЦвет телефона: blue\nВес телефона (гр.): 169\nОбъем оперативной памяти телефона (Гб): 4\nОбъем встроенной памяти телефона (Гб): 64")

@dp.message_handler(text='Xiaomi Redmi 6')
async def front3(message: types.Message):
    await message.reply("""https://i0.wp.com/techshop.kg/wp-content/uploads/2019/01/0d35816c92b4fa818cbf69f33fcfe969.jpg?resize=300%2C300&ssl=1""")
    await message.answer("Xiaomi Redmi 6 64 Gb (RAM 4 Gb) EU black")
    await message.answer("10,299 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nОперационная система телефона: Android\nВерсия ОС телефона : Android 8.1\nКоличество SIM-карт телефона: 2\nЦвет телефона: black\nВес телефона (гр.): 146\nВстроенная вспышка в телефоне\nОбъем оперативной памяти телефона (Гб): 4\nОбъем встроенной памяти телефона (Гб): 64")

@dp.message_handler(text='Xiaomi Redmi Note 6 Pro(black)')
async def front4(message: types.Message):
    await message.reply("""https://i2.wp.com/techshop.kg/wp-content/uploads/2019/01/c00ec1c8c809f54fca1f6b41797db2cc.jpg?resize=150%2C150&ssl=1""")
    await message.answer("Xiaomi Redmi Note 6 Pro 64 Gb (RAM 4 Gb) black")
    await message.answer("13,660 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА \nОперационная система телефона: Android\nВерсия ОС телефона : Android 8.1\nКоличество SIM-карт телефона:2\nЦвет телефона: black\nОбъем оперативной памяти телефона (Гб): 4\nОбъем встроенной памяти телефона (Гб): 64")

@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await pro(message)

iph=[
    types.KeyboardButton("iPhone Xs 64GB Silver"),
    types.KeyboardButton("iPhone 8 +"),
    types.KeyboardButton("iPhone 8"),
    types.KeyboardButton("Назад")
]

iph_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*iph)

@dp.message_handler(text='iPhone')
async def kind_iphone(message: types.Message):
    await message.answer("Выбираете", reply_markup=iph_keyboard)

@dp.message_handler(text="iPhone Xs 64GB Silver")
async def iph1(message: types.Message):
    await message.reply("""https://i0.wp.com/techshop.kg/wp-content/uploads/2018/12/52979-big.jpg?resize=300%2C300&ssl=1""")
    await message.answer("iPhone Xs 64GB Silver")
    await message.answer("79,854 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nСмартфон iPhone Xs Max обладает хорошей камерой на 12+12 Мп и мощным процессор A12 Bionic. Оперативной памяти на 4 ГБ хватает для стабильной работы системы, объем встроенной памяти составляет 64 ГБ")

@dp.message_handler(text="iPhone 8 +")
async def iph2(message: types.Message):
    await message.reply("""https://i2.wp.com/techshop.kg/wp-content/uploads/2018/09/smartfon-apple-iphone-8-plus-64gb-gold.jpg?resize=300%2C300&ssl=1""")
    await message.answer("iPhone 8 +")
    await message.answer("53,707 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nВпервые передняя и задняя панели iPhone выполнены из стекла. Самая популярная камера усовершенствована. Установлен самый умный и мощный процессор, когда-либо созданный для iPhone. Без проводов процесс зарядки становится элементарным. А дополненная реальность открывает невиданные до сих пор возможности. iPhone 8. Новое поколение iPhone.")

@dp.message_handler(text='iPhone 8')
async def iph3(message:types.Message):
    await message.reply("""https://i1.wp.com/techshop.kg/wp-content/uploads/2018/09/4c4aed40acb32ae5b5d56930a36bac77-1000x1000.jpg?resize=300%2C300&ssl=1""")
    await message.answer("iPhone 8")
    await message.answer("44,988 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nХарактеристики\nПроцессор: 2100 Мгц (6-ядерный), граф.процессор\n Память: 64 Гб, 2 Гб RAM\n Платформа: IOS 11\n Аккумулятор: 1821 мА*ч Li-Ion, 14 ч разг.(GSM), 14 ч разг.(WCDMA)\nЭкран: 4.7″, сенсорный, 1334×750, емкостный, IPS, 16 млн.цв.\nКамера: 12 мпикс, 4619×2598, 5X цифр зум, вспышка 4-светодиода \nВид: Моноблок, 148 г, 138.4×67.3×7.3 мм")

@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await pro(message)



huawei=[
    types.KeyboardButton("Huawei Y5 Prime"),
    types.KeyboardButton("Huawei P Smart"),
    types.KeyboardButton("Huawei P8 Lite"),
    types.KeyboardButton("Назад")
]

huawei_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*huawei)

@dp.message_handler(text='Huawei')
async def kind_huawei(message: types.Message):
    await message.answer("Выбираете", reply_markup=huawei_keyboard)

@dp.message_handler(text='Huawei Y5 Prime')
async def hai1(message: types.Message):
    await message.answer("""https://i0.wp.com/techshop.kg/wp-content/uploads/2018/08/4435388.jpg?resize=300%2C300&ssl=1""")
    await message.answer("Huawei Y5 Prime")
    await message.answer("16,000 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nПроцессор: 1500 Мгц (4-ядерный), граф.процессор\nПамять: 16 Гб + 256 Гб, 2 Гб RAM, microSDXC, microSDHC\nПлатформа: Android 8.0\nАккумулятор: 3020 мА*ч Li-Ion, зарядка от USB, несъемная батарея\nЭкран: 5.45″, сенсорный, 1440×720, емкостный, IPS, 16 млн.цв.\nКамера: 13 мпикс, 4807×2704, вспышка, детектор лиц, автофокус\nВид: Моноблок, 145 г, 146.5×70.9×8.3 мм")

@dp.message_handler(text='Huawei P Smart')
async def hai2(message: types.Message):
    await message.reply("""https://i0.wp.com/techshop.kg/wp-content/uploads/2018/08/psmart.jpeg?resize=150%2C150&ssl=1""")
    await message.answer("Huawei P Smart")
    await message.answer("14,900 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nПроцессор: 2360 Мгц (8-ядерный), граф.процессор\nПамять: 32 Гб + 256 Гб, 3 Гб RAM, microSDXC, microSDHC\nПлатформа: Android 8.0\nАккумулятор: 3000 мА*ч Li-Pol, зарядка от USB, несъемная батарея\nЭкран: 5.65″, сенсорный, 2160×1080, емкостный, IPS\nКамера: 13 мпикс, 4807×2704, вспышка, детектор лиц, автофокус\nВид: Моноблок, 143 г, 150.1×72.1×7.5 мм")

@dp.message_handler(text='Huawei P8 Lite')
async def hai3(message: types.Message):
    await message.reply("""https://i0.wp.com/techshop.kg/wp-content/uploads/2018/08/i.jpg?resize=150%2C150&ssl=1""")
    await message.reply("Huawei P8 Lite")
    await message.answer("11,900 сом")
    await message.answer(f"ОБЩИЕ ХАРАКТЕРИСТИКИ ТЕЛЕФОНА\nПроцессор: 2100 Мгц (8-ядерный), граф.процессор\nПамять: 16 Гб + 128 Гб, 3 Гб RAM, microSDXC, microSDHC\nПлатформа: Android 7.0\nАккумулятор: 3000 мА*ч Li-Pol, 36 ч разг.(GSM), 21 ч разг.(WCDMA)\nЭкран: 5.2″, сенсорный, 1920×1080, емкостный, IPS, 16 млн.цв.\nКамера: 12 мпикс, 4619×2598, вспышка, детектор лиц, автофокус\nВид: Моноблок, 147 г, 147.2×72.9×7.6 мм")

@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await pro(message)



@dp.message_handler(text='заказать')
async def order(message: types.Message):
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact_info = f"Контакт: {message.contact.phone_number}, Имя: {message.contact.first_name}, Фамилия: {message.contact.last_name}"
    await message.answer(contact_info)
    await bot.send_message(1836987628, contact_info)
    await message.answer("Артикул товара который вы хотите заказать:")

@dp.message_handler(text="Назад")
async def back_start1(message:types.Message):
    await start(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
