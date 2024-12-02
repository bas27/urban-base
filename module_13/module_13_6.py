from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

inline_kb = InlineKeyboardMarkup()
button_i = InlineKeyboardButton(text='Информация', callback_data='info')
button_i_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_i_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.row(button_i_calc, button_i_formulas)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [button_info],
        [button_calc,
         KeyboardButton(text='Параметры')]
    ],
    resize_keyboard=True
)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите действие', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(10 x вес(кг) + 6.25 x рост(см) + 5 x возраст(лет) + 5) x мин.активность')
    await call.answer()


@dp.callback_query_handler(text='info')
async def infor(call):
    await call.message.answer('Информация о боте инлайн')
    await call.answer()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте')


class UserState(StatesGroup):
    address = State()
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
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
    calories = ((10 * int(data['weight'])) + (6.25 * int(data['growth'])) + (5 * int(data['age'])) + 5) * 1.2
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
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


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
