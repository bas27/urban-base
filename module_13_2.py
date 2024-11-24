from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import secret

token = secret.token
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text=['Привет', 'Пока'])
async def all_message(message):
    print('Вывод отдельного сообщения')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
