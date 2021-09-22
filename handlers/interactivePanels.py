from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import bot

from utils import file_system
from loader import dp
from states.interactivePanels import InteractivePanels
from keyboards.keyboards import *

from report import report

from datetime import datetime


@dp.message_handler(commands=['test'])
async def enter_test(message: types.Message):
    await message.answer("Вы начали экспертизу интерактивной панели.\n"
                         "Введите серийный номер устройства:")
    await InteractivePanels.Serial.set()


@dp.message_handler(state=InteractivePanels.Serial)
async def enter_serial(message: types.Message, state: FSMContext):
    answer = message.text
    date = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    type = "Интерактивная панель"
    async with state.proxy() as data:
        data["date"] = date
        data["type"] = type
        data["serial"] = answer

    await message.answer("Сделайте фотографию внешнего вида интерактивной панели и отправьте её сюда:")

    await InteractivePanels.next()


@dp.message_handler(state=InteractivePanels.Photo, content_types=['photo'])
async def save_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = f'{data["serial"]}.jpg'
    await message.photo[-1].download(f'photos/{data["serial"]}.jpg')

    if "yes_no" in file_system.read('interactivePanels')['1'][0]:
        await message.answer(file_system.read('interactivePanels')['1'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['1'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()


# УНИВЕРСАЛЬНЫЙ ХЭНДЛЕР
@dp.message_handler(state=InteractivePanels.Question)
async def answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    for question in file_system.read('interactivePanels'):
        if f"Q{str(question)}" not in data:
            await InteractivePanels.Question.set()
            if str(int(question)+1) in file_system.read('interactivePanels'):
                if "yes_no" in file_system.read('interactivePanels')[str(int(question)+1)][0]:
                    await message.answer(file_system.read('interactivePanels')[str(int(question)+1)][1], reply_markup=yes_no)
                elif "text" in file_system.read('interactivePanels')[str(int(question)+1)][0]:
                    await message.answer(file_system.read('interactivePanels')[str(int(question)+1)][1], reply_markup=ReplyKeyboardRemove())
                async with state.proxy() as data:
                    data[f"Q{str(question)}"] = message.text
                    break
            else:
                async with state.proxy() as data:
                    data[f"Q{str(question)}"] = message.text
                data = await state.get_data()
                await message.answer(f"Экспертиза панели с серийным номером {data['serial']} завершена\n"
                                        "Для проведения экспертизы другой интерактивной панели выберите команду /test",  reply_markup=ReplyKeyboardRemove())
                try:
                    report(data)
                    await bot.send_document(message.from_user.id, InputFile(f"reports/reportPanel-{data['serial']}.pdf"))
                except Exception as e:
                    await message.answer("Произошла ошибка при формировании отчета.",  reply_markup=ReplyKeyboardRemove()) 
                await state.finish()
