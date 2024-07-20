from aiogram import Bot,Dispatcher,types,executor
from hmw4 import result
from config import token

bot=Bot(token=token)
dp = Dispatcher(bot)
# num  = [1,2,3]
# random_num = random.choice(num)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('привет!')
    await message.answer("Я загадал число от 1 до 3 угадайте")

@dp.message_handler(text='1')
async def cmd_one(message: types.Message):
    if result == 1:
        await message.answer('Правильно вы отгадали! ')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer('Вы проиграли!')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text='2')
async def cmd_two(message: types.Message):
    if result == 2:
        await message.answer('Правильно вы отгадали! ')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer('Вы проиграли!')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text='3')
async def cmd_three(message: types.Message):
    if result == 3:
        await message.answer('Правильно вы отгадали! ')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer('Вы проиграли!')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")


executor.start_polling(dp, skip_updates = True)