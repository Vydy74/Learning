from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties

import asyncio



api = ""
bot = Bot(token=api, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message(F.text)
async def cmd_message(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
