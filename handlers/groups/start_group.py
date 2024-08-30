from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from filters.group_filter import IsGroup
from keyboards.inline.inline_keyboards import check_inline

@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!")