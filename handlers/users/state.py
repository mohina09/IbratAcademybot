from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp, db, bot
from states.personal_data import PersonalData
from keyboards.default.default_keyboards import ha_yoq_btn, telefon_btn
from data.config import ADMINS
from aiogram.utils import exceptions as aiogram_exceptions
import sqlite3

@dp.message_handler(commands="alluser", user_id=ADMINS)
async def all_user(message: types.Message):

    @dp.callback_query_handler(text="ha")
    async def ha_(calls: types.CallbackQuery):
        await calls.message.delete()
        await calls.message.answer("Ism, familiyangizni kiriting?")
        await PersonalData.fullName.set()


    @dp.message_handler(state=PersonalData.fullName)
    async def answer_fullname(message: types.Message, state: FSMContext):
        fullname = message.text

        await state.update_data(
            {"To'liq ismingiz: ": fullname}
        )
        await message.answer("Emailingizni kiriting")
        await PersonalData.next()


    @dp.message_handler(state=PersonalData.email)
    async def answer_email(message: types.Message, state: FSMContext):
        email_ = message.text

        await state.update_data(
            {"Email: " : email_}
        )
        await message.answer("Telefon raqamingizni qoldiring.", reply_markup=telefon_btn)
        await PersonalData.next()


    @dp.message_handler(state=PersonalData.phoneNum)
    async def answer_phonenum(message: types.Message, state: FSMContext):
        phonenum = message.text

        await state.update_data(
            {"Telefon raqamingiz: ": phonenum}
        )

        data_ = await state.get_data()
        fullname = data_.get("To'liq ismingiz: ")
        email_ = data_.get("Email: ")
        phonenum = data_.get("Telefon raqamingiz: ")


        msg = "Admin bilan bog'lanish uchun ma'lumotlar:\n\n"
        msg += f"👥Toliq ismingiz: {fullname}\n\n"
        msg += f"📧Email: {email_}\n\n"
        msg += f"📞Telefon raqamingiz: {phonenum}\n\n"
        await message.answer("Kiritilgan barcha ma'lumotlar to'grimi?", reply_markup=ha_yoq_btn)
        await message.answer(msg)

        await state.reset_state()

    text = ""
    users = db.select_all_users()
    for user in users:
            text += f"""Admin bilan bog'lanish uchun ma'lumotlar:\n\n
        User_name: {message.from_user.full_name}\n\n
        👥Toliq ismingiz: {fullname}\n\n
        📧Email: {email_}\n\n
        📞Telefon raqamingiz: {phonenum}\n\n"""

    await bot.send_message(chat_id=ADMINS[0], text=text)