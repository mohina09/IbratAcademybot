from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from loader import dp, db, bot
from utils.notify_admins import ADMINS
from keyboards.default.default_keyboards import start_btn
from filters.private_filter import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!")
    await message.answer("Xush kelibsiz!")
    await message.answer("Ingliz tilidan levelingiz tanlang👇:", reply_markup=start_btn)
    name = message.from_user.full_name

    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)


    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)