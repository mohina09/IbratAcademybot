from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command("phone"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Telefon raqamingizni yuboring")
    await state.set_state("telefon")


@dp.message_handler(state="telefon")
async def enter_email(message: types.Message, state: FSMContext):
    telefon = message.text
    db.update_user_phone(phone=telefon, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Baza yangilandi: {user}")
    await state.finish()