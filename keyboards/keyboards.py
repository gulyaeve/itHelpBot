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

request_submit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить")
        ],
        [
            KeyboardButton(text="ОТМЕНА")
        ],
    ],
    resize_keyboard=True
    )

