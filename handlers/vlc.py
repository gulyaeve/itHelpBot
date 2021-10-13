from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Command
from loader import bot

import re
from utils import file_system
from loader import dp
from keyboards.keyboards import *

from video import videoScreen

from datetime import datetime

pattern = r"(?:10.)\d{1,}.\d{1,}.\d{1,}:\d{1,}"

class Vlc(StatesGroup):
    Serial = State()

@dp.message_handler(commands=['test'])
async def enter_test(message: types.Message):
    await message.answer("Вы начали проверку ракурса видеокамеры.\n"
                         "Для отмены: /cancel.\n"
                         "Введите ip-адрес и порт устройства в формате: 10.x.x.x:8899")
    await Vlc.Serial.set()


@dp.message_handler(state=Vlc.Serial)
async def enter_serial(message: types.Message, state: FSMContext):
    if re.findall(pattern, message.text):
        await message.answer("В течение минуты вы получите скриншот с камеры.")
        try:
            await videoScreen(message.text, message.from_user.username)
            await bot.send_photo(message.from_user.id, InputFile(f"screens/{message.text.split(':')[0]}-{message.from_user.username}.png"))
        except Exception as e:
            await message.answer("Произошла ошибка соединения.\n"
                                 "1. Проверьте ip-адрес трансляции. Укажите в формате 10.хх.хх.хх:8899\n"
                                 "2. Обновите VLC (в некоторых случаях при переустановке программа предлагает установить дополнительные разрешения на трансляцию) videolan.org/vlc/\n\n"
                                 "Если ошибка повторяется напишите организаторам. it-help@edu.mos.ru")
    else:
        return await message.answer("Неверный формат ввода.")

    await state.finish()