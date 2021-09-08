from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
    ],
    resize_keyboard=True
    )
