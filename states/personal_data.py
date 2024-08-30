from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards.default.default_keyboards import telefon_btn


class PersonalData(StatesGroup):
    fullName = State()
    email = State()
    phoneNum = State()