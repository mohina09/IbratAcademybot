from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="A1 | Beginner📕"),
            KeyboardButton(text="A2 | Elementry📗")
        ],
        [
            KeyboardButton(text="A2-B1 | Pre-Intermediate📘"),
            KeyboardButton(text="B1 | Intermediate📙")
        ],
        [
            KeyboardButton(text="B2 | Upper-Intermediate📔")
        ],
        [
            KeyboardButton(text="Admin bilan bog'lanish📲")
        ]
    ],
    resize_keyboard=True
)


ha_yoq_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha✅"),
            KeyboardButton(text="Yo'q❌")
        ]
    ],
    resize_keyboard=True
)


telefon_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam qoldirish📱", request_contact=True)
        ]
    ],
    resize_keyboard=True
)