from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
import secret

token = secret.token
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')

button_calc = KeyboardButton(text='Рассчитать')
kb.row(button_info, button_calc)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте')

class UserState(StatesGroup):
    address = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = ((10 * int(data['weight'])) + (6.25 * int(data['growth'])) + (5 * int(data['age']))) * 1.2
    await message.answer(f'Ваша норма колорий при минимальной активности составляет: {calories}')
    await state.finish()


@dp.message_handler(text='Заказать')
async def buy(message):
    await message.answer('Отправь нам свой адрес, пожалуйста')
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(address=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, адрес сохранен: {data["address"]}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Привет', 'Пока'])
async def all_message(message):
    print('Вывод отдельного сообщения')
    # await bot.send_message(message.from_user.id, 'Привет!')
    await message.answer('Привет!')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)