import asyncio
import re
import threading
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile, ReplyKeyboardRemove

from loader import bot
from loader import dp
from keyboards.keyboards import *
from video import videoScreen, videoScreen2

pattern = r"(?:10.)\d{1,}.\d{1,}.\d{1,}:\d{1,}"
pattern2 = r"(?:10.)\d{1,}.\d{1,}.\d{1,}"


class Vlc(StatesGroup):
    Technology = State()
    Hostname = State()
    HostnameECHD = State()


@dp.message_handler(commands=['help'])
async def enter_test(message: types.Message):
    await message.answer("Инструкция по настройке доступна по ссылке:\n"
                         "https://connect.temocenter.ru/files/video18-19oct.pdf")


@dp.message_handler(commands=['test'])
async def cam_option(message: types.Message):
    await message.answer("Вы начали проверку ракурса видеокамеры.\n"
                         "Для отмены: /cancel.\n"
                         "Выберите технологию, по которой работает данная камера:",
                         reply_markup=vlc_echd)
    await Vlc.Technology.set()


@dp.message_handler(state=Vlc.Technology)
async def enter_technology(message: types.Message):
    if message.text == "VLC":
        await message.answer("Введите ip-адрес и порт устройства в формате: 10.x.x.x:8899", reply_markup=ReplyKeyboardRemove())
        await Vlc.Hostname.set()
    elif message.text == "ЕЦХД":
        await message.answer("Введите ip-адрес устройства в формате: 10.x.x.x", reply_markup=ReplyKeyboardRemove())
        await Vlc.HostnameECHD.set()
    else:
        return await message.answer(
            "Неверный формат ввода.")


@dp.message_handler(state=Vlc.Hostname)
async def enter_serial(message: types.Message, state: FSMContext):
    if re.match(pattern, message.text):
        date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        user = message.from_user.id
        x = threading.Thread(target=videoScreen, args=(message.text, user, date_now))
        x.start()
        await message.answer("В течение минуты вы получите скриншот с камеры.")
        try:
            await asyncio.sleep(20)
            await bot.send_photo(message.from_user.id,
                                 InputFile(
                                     f"screens/VLC-{message.text.split(':')[0]}-{user}-{date_now}.png"))
        except Exception as e:
            await message.answer("Произошла ошибка соединения.\n"
                                 "1. Проверьте ip-адрес трансляции. Укажите в формате 10.хх.хх.хх:8899\n"
                                 "2. Обновите VLC (в некоторых случаях при переустановке программа предлагает "
                                 "установить дополнительные разрешения на трансляцию) videolan.org/vlc/\n\n "
                                 "Если ошибка повторяется напишите организаторам. it-help@edu.mos.ru\n\n")
    else:
        return await message.answer(
            "Неверный формат ввода. Введите ip-адрес и порт устройства в формате: 10.x.x.x:8899")
    await message.answer("Используйте команду /test для повторного запуска проверки видеокамеры.")
    await state.finish()


@dp.message_handler(state=Vlc.HostnameECHD)
async def send_video(message: types.Message, state: FSMContext):
    if re.match(pattern2, message.text):
        date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        user = message.from_user.id
        x = threading.Thread(target=videoScreen2, args=(message.text, user, date_now))
        x.start()
        await message.answer("В течение минуты вы получите скриншот с камеры.")
        try:
            await asyncio.sleep(20)
            await bot.send_photo(message.from_user.id,
                                 InputFile(
                                     f"screens/ECHD-{message.text}-{user}-{date_now}.png"))
        except Exception as e:
            await message.answer("Произошла ошибка соединения.\n"
                                 "Проверьте ip-адрес трансляции. Укажите в формате 10.хх.хх.хх\n"
                                 "Если ошибка повторяется напишите организаторам. it-help@edu.mos.ru\n\n")
    else:
        return await message.answer(
            "Неверный формат ввода. Введите ip-адрес устройства в формате: 10.x.x.x")
    await message.answer("Используйте команду /test для повторного запуска проверки видеокамеры.")
    await state.finish()
