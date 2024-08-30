from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.private_filter import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("🆘Yordam kerak bo'lsa adminga murojaat qiling. \n\n https://t.me/mohinakhon09")