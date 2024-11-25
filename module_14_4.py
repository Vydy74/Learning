from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from pathlib import Path
from aiogram.types import FSInputFile
from crud_functions import initiate_db, get_all_products

api = "6157846986:AAHBUwqwzWgbj0xxkWfIrDE7yYFsnu372_Q"

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
initiate_db()

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'),
                                  KeyboardButton(text='Информация')],
                                  [KeyboardButton(text='Купить')],
                                  [KeyboardButton(text='Регистрация')]],
                        resize_keyboard=True)

ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
                                          [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]])

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(Command("start"))
async def starter(message: Message):
    await message.answer("Привет! Для расчета нормы калорий нажмите 'Рассчитать'.", reply_markup=kb)

@dp.message(F.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=ikb)

@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    formula_text = ("Формула Миффлина-Сан Жеора для женщин:\n"
                    "Калории = (10 x вес в кг) + (6.25 x рост в см) - (5 x возраст в годах) - 161")
    await call.message.answer(formula_text)
    await call.answer()

@dp.callback_query(F.data == 'calories')
async def set_age(call: CallbackQuery, state):
    await call.message.answer("Отправь свой возраст в годах")
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message: Message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост в см")
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: Message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес в кг")
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: Message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age'))
    growth = float(data.get('growth'))
    weight = float(data.get('weight'))

    cal = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f"Ваша суточная норма калорий = {cal} калорий")
    await state.clear()

@dp.message(F.text == 'Купить')
async def get_buying_list(message: Message):
    products = get_all_products()

    if not products:
        await message.answer("Список продуктов пока пуст.")
        return

    # Вывод информации о продуктах
    for index, product in enumerate(products, start=1):
        product_id, title, description, price = product
        product_info = f"Название: {title}\nОписание: {description}\nЦена: {price} руб."
        await message.answer(product_info)

        photo_path = Path(f'files/image{index}.jpg')

        if photo_path.exists():
            photo = FSInputFile(photo_path)
            await message.answer_photo(photo)
        else:
            await message.answer("Изображение для данного продукта отсутствует.")

    # Отображение кнопок для покупки
    imenu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"Продукт {product[0]}", callback_data='product_buying')]
            for product in products
        ]
    )
    await message.answer("Выберите продукт для покупки:", reply_markup=imenu)


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == "__main__":
    dp.run_polling(bot)