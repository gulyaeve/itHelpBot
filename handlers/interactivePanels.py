from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from utils import file_system
from loader import dp
from states.interactivePanels import InteractivePanels


@dp.message_handler(commands=['test'])
async def enter_test(message: types.Message):
    await message.answer("Вы начали экспертизу интерактивной панели.\n"
                         "Введите серийный номер устройства:")
    await InteractivePanels.Serial.set()


@dp.message_handler(state=InteractivePanels.Serial)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["serial"] = answer

    await message.answer(file_system.read('interactivePanels')['1'])

    await InteractivePanels.next()


@dp.message_handler(state=InteractivePanels.Q1)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    # data = await state.get_data()
    # answer1 = data.get("answer1")
    # answer2 = message.text
    async with state.proxy() as data:
        data["Q1"] = answer

    await message.answer("Спасибо за ваши ответы!")

    await state.finish()

    # Вариант без стирания данных в data
    # await state.reset_state(with_data=False)
