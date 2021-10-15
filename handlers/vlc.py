import asyncio
import re
import threading
from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from loader import bot
from loader import dp
from video import videoScreen, videoCap

pattern = r"(?:10.)\d{1,}.\d{1,}.\d{1,}:\d{1,}"


class Vlc(StatesGroup):
    Hostname = State()
    Video = State()


@dp.message_handler(commands=['help'])
async def enter_test(message: types.Message):
    await message.answer("Инструкция по настройке доступна по ссылке:\n"
                         "https://connect.temocenter.ru/files/video18-19oct.pdf")


@dp.message_handler(commands=['test'])
async def enter_test(message: types.Message):
    await message.answer("Вы начали проверку ракурса видеокамеры.\n"
                         "Для отмены: /cancel.\n"
                         "Введите ip-адрес и порт устройства в формате: 10.x.x.x:8899")
    await Vlc.Hostname.set()


@dp.message_handler(state=Vlc.Hostname)
async def enter_serial(message: types.Message, state: FSMContext):
    if re.match(pattern, message.text):
        date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        x = threading.Thread(target=videoScreen, args=(message.text, message.from_user.username, date_now))
        x.start()
        await message.answer("В течение минуты вы получите скриншот с камеры.")
        try:
            await asyncio.sleep(15)
            await bot.send_photo(message.from_user.id,
                                 InputFile(
                                     f"screens/{message.text.split(':')[0]}-{message.from_user.username}-{date_now}.png"))
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


@dp.message_handler(commands=['video'])
async def enter_test(message: types.Message):
    await message.answer("Я отправлю вам видео с камеры, длительностью 5 секунд.\n"
                         "Для отмены: /cancel.\n"
                         "Введите ip-адрес и порт устройства в формате: 10.x.x.x:8899")
    await Vlc.Video.set()


@dp.message_handler(state=Vlc.Video)
async def send_video(message: types.Message, state: FSMContext):
    if re.match(pattern, message.text):
        date_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        x = threading.Thread(target=videoCap, args=(message.text, message.from_user.username, date_now))
        x.start()
        await message.answer("В течение минуты вы получите видео с камеры.")
        try:
            await asyncio.sleep(20)
            path_to_file = f"videos/{message.text.split(':')[0]}-{message.from_user.username}-{date_now}.mp4"
            await bot.send_video(message.from_user.id, InputFile(path_to_file))
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
