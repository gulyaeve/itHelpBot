from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Command
from loader import bot

from utils import file_system
from loader import dp
from keyboards.keyboards import *

from video import videoScreen

from datetime import datetime

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
    # filename = message.text.split(":")[0]
    videoScreen(message.text)
    await bot.send_document(message.from_user.id, InputFile(f"screens/{message.text.split(':')[0]}.png"))

    await state.finish()