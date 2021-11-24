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

vlc_echd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="VLC"),
            KeyboardButton(text="ЕЦХД")
        ],
    ],
    resize_keyboard=True
    )
