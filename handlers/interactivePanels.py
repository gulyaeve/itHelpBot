from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from utils import file_system
from loader import dp
from states.interactivePanels import InteractivePanels
from keyboards.keyboards import *


@dp.message_handler(commands=['test'])
async def enter_test(message: types.Message):
    await message.answer("Вы начали экспертизу интерактивной панели.\n"
                         "Введите серийный номер устройства:")
    await InteractivePanels.Serial.set()


@dp.message_handler(state=InteractivePanels.Serial)
async def enter_serial(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["serial"] = answer

    await message.answer("Сделайте фотографию внешнего вида интерактивной панели и отправьте её сюда:")

    await InteractivePanels.next()


@dp.message_handler(state=InteractivePanels.Photo, content_types=['photo'])
async def save_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = f'{data["serial"]}.jpg'
    await message.photo[-1].download(f'photos/{data["serial"]}.jpg')
    print(data)

    await message.answer(file_system.read('interactivePanels')['1'], reply_markup=yes_no)

    await InteractivePanels.next()



@dp.message_handler(state=InteractivePanels.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Q1"] = answer

    await message.answer(file_system.read('interactivePanels')['2'], reply_markup=yes_no)

    await InteractivePanels.next()


@dp.message_handler(state=InteractivePanels.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Q2"] = answer

    await message.answer(file_system.read('interactivePanels')['3'], reply_markup=yes_no)

    await InteractivePanels.next()
