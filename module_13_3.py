from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = " "
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_massages(message):
    await message.reply(message.text.upper())
    await message.answer("Введите команду /start, чтобы начать общение.")

async def main():
    await dp.start_polling(dp)

if __name__ == '__main__':
    asyncio.run(main())