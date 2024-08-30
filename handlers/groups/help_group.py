from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from filters.group_filter import IsGroup

@dp.message_handler(IsGroup(), CommandHelp())
async def heelp(message: types.Message):
    await message.answer("Yordam kerak bo'lsa adminga murojaat qiling.\n\nhttps://t.me/mohinakhon09")