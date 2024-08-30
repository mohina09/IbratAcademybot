import time
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.utils import exceptions as aiogram_exceptions


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def all_users(message: types.Message):
    text = ""
    users = db.select_all_users()
    for user in users:
        text += f"ID: {user[0]} Ism: {user[1]} Email: {user[2]} Telefon raqami: {user[3]}\n"

    # print(users[0][0])
    await message.answer(text)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def reklama(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        print(user_id)
        try:
            await bot.send_message(chat_id=user_id, text="Reklama")
        except aiogram_exceptions.BotBlocked:
            pass


@dp.message_handler(text="/cleardb", user_id=ADMINS)
async def cleardb(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
