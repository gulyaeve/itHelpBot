from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove
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

    if "yes_no" in file_system.read('interactivePanels')['1'][0]:
        await message.answer(file_system.read('interactivePanels')['1'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['1'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()


@dp.message_handler(state=InteractivePanels.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q1'] = answer

    if "yes_no" in file_system.read('interactivePanels')['2'][0]:
        await message.answer(file_system.read('interactivePanels')['2'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['2'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q2'] = answer

    if "yes_no" in file_system.read('interactivePanels')['3'][0]:
        await message.answer(file_system.read('interactivePanels')['3'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['3'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q3'] = answer

    if "yes_no" in file_system.read('interactivePanels')['4'][0]:
        await message.answer(file_system.read('interactivePanels')['4'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['4'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q4'] = answer

    if "yes_no" in file_system.read('interactivePanels')['5'][0]:
        await message.answer(file_system.read('interactivePanels')['5'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['5'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q5'] = answer

    if "yes_no" in file_system.read('interactivePanels')['6'][0]:
        await message.answer(file_system.read('interactivePanels')['6'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['6'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q6'] = answer

    if "yes_no" in file_system.read('interactivePanels')['7'][0]:
        await message.answer(file_system.read('interactivePanels')['7'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['7'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q7'] = answer

    if "yes_no" in file_system.read('interactivePanels')['8'][0]:
        await message.answer(file_system.read('interactivePanels')['8'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['8'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q8'] = answer

    if "yes_no" in file_system.read('interactivePanels')['9'][0]:
        await message.answer(file_system.read('interactivePanels')['9'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['9'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q9'] = answer

    if "yes_no" in file_system.read('interactivePanels')['10'][0]:
        await message.answer(file_system.read('interactivePanels')['10'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['10'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q10)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q10'] = answer

    if "yes_no" in file_system.read('interactivePanels')['11'][0]:
        await message.answer(file_system.read('interactivePanels')['11'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['11'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q11)
async def answer_q11(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q11'] = answer

    if "yes_no" in file_system.read('interactivePanels')['12'][0]:
        await message.answer(file_system.read('interactivePanels')['12'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['12'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q12)
async def answer_q12(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q12'] = answer

    if "yes_no" in file_system.read('interactivePanels')['13'][0]:
        await message.answer(file_system.read('interactivePanels')['13'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['13'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q13)
async def answer_q13(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q13'] = answer

    if "yes_no" in file_system.read('interactivePanels')['14'][0]:
        await message.answer(file_system.read('interactivePanels')['14'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['14'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q14)
async def answer_q14(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q14'] = answer

    if "yes_no" in file_system.read('interactivePanels')['15'][0]:
        await message.answer(file_system.read('interactivePanels')['15'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['15'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q15)
async def answer_q15(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q15'] = answer

    if "yes_no" in file_system.read('interactivePanels')['16'][0]:
        await message.answer(file_system.read('interactivePanels')['16'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['16'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q16)
async def answer_q16(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q16'] = answer

    if "yes_no" in file_system.read('interactivePanels')['17'][0]:
        await message.answer(file_system.read('interactivePanels')['17'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['17'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q17)
async def answer_q17(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q17'] = answer

    if "yes_no" in file_system.read('interactivePanels')['18'][0]:
        await message.answer(file_system.read('interactivePanels')['18'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['18'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q18)
async def answer_q18(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q18'] = answer

    if "yes_no" in file_system.read('interactivePanels')['19'][0]:
        await message.answer(file_system.read('interactivePanels')['19'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['19'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q19)
async def answer_q19(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q19'] = answer

    if "yes_no" in file_system.read('interactivePanels')['20'][0]:
        await message.answer(file_system.read('interactivePanels')['20'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['20'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q20)
async def answer_q20(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q20'] = answer

    if "yes_no" in file_system.read('interactivePanels')['21'][0]:
        await message.answer(file_system.read('interactivePanels')['21'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['21'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q21)
async def answer_q21(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q21'] = answer

    if "yes_no" in file_system.read('interactivePanels')['22'][0]:
        await message.answer(file_system.read('interactivePanels')['22'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['22'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q22)
async def answer_q22(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q22'] = answer

    if "yes_no" in file_system.read('interactivePanels')['23'][0]:
        await message.answer(file_system.read('interactivePanels')['23'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['23'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q23)
async def answer_q23(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q23'] = answer

    if "yes_no" in file_system.read('interactivePanels')['24'][0]:
        await message.answer(file_system.read('interactivePanels')['24'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['24'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q24)
async def answer_q24(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q24'] = answer

    if "yes_no" in file_system.read('interactivePanels')['25'][0]:
        await message.answer(file_system.read('interactivePanels')['25'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['25'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q25)
async def answer_q25(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q25'] = answer

    if "yes_no" in file_system.read('interactivePanels')['26'][0]:
        await message.answer(file_system.read('interactivePanels')['26'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['26'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q26)
async def answer_q26(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q26'] = answer

    if "yes_no" in file_system.read('interactivePanels')['27'][0]:
        await message.answer(file_system.read('interactivePanels')['27'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['27'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q27)
async def answer_q27(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q27'] = answer

    if "yes_no" in file_system.read('interactivePanels')['28'][0]:
        await message.answer(file_system.read('interactivePanels')['28'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['28'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q28)
async def answer_q28(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q28'] = answer

    if "yes_no" in file_system.read('interactivePanels')['29'][0]:
        await message.answer(file_system.read('interactivePanels')['29'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['29'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q29)
async def answer_q29(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q29'] = answer

    if "yes_no" in file_system.read('interactivePanels')['30'][0]:
        await message.answer(file_system.read('interactivePanels')['30'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['30'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q30)
async def answer_q30(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q30'] = answer

    if "yes_no" in file_system.read('interactivePanels')['31'][0]:
        await message.answer(file_system.read('interactivePanels')['31'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['31'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q31)
async def answer_q31(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q31'] = answer

    if "yes_no" in file_system.read('interactivePanels')['32'][0]:
        await message.answer(file_system.read('interactivePanels')['32'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['32'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q32)
async def answer_q32(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q32'] = answer

    if "yes_no" in file_system.read('interactivePanels')['33'][0]:
        await message.answer(file_system.read('interactivePanels')['33'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['33'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q33)
async def answer_q33(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q33'] = answer

    if "yes_no" in file_system.read('interactivePanels')['34'][0]:
        await message.answer(file_system.read('interactivePanels')['34'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['34'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q34)
async def answer_q34(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q34'] = answer

    if "yes_no" in file_system.read('interactivePanels')['35'][0]:
        await message.answer(file_system.read('interactivePanels')['35'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['35'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q35)
async def answer_q35(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q35'] = answer

    if "yes_no" in file_system.read('interactivePanels')['36'][0]:
        await message.answer(file_system.read('interactivePanels')['36'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['36'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q36)
async def answer_q36(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q36'] = answer

    if "yes_no" in file_system.read('interactivePanels')['37'][0]:
        await message.answer(file_system.read('interactivePanels')['37'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['37'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q37)
async def answer_q37(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q37'] = answer

    if "yes_no" in file_system.read('interactivePanels')['38'][0]:
        await message.answer(file_system.read('interactivePanels')['38'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['38'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q38)
async def answer_q38(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q38'] = answer

    if "yes_no" in file_system.read('interactivePanels')['39'][0]:
        await message.answer(file_system.read('interactivePanels')['39'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['39'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q39)
async def answer_q39(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q39'] = answer

    if "yes_no" in file_system.read('interactivePanels')['40'][0]:
        await message.answer(file_system.read('interactivePanels')['40'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['40'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q40)
async def answer_q40(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q40'] = answer

    if "yes_no" in file_system.read('interactivePanels')['41'][0]:
        await message.answer(file_system.read('interactivePanels')['41'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['41'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q41)
async def answer_q41(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q41'] = answer

    if "yes_no" in file_system.read('interactivePanels')['42'][0]:
        await message.answer(file_system.read('interactivePanels')['42'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['42'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q42)
async def answer_q42(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q42'] = answer

    if "yes_no" in file_system.read('interactivePanels')['43'][0]:
        await message.answer(file_system.read('interactivePanels')['43'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['43'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q43)
async def answer_q43(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q43'] = answer

    if "yes_no" in file_system.read('interactivePanels')['44'][0]:
        await message.answer(file_system.read('interactivePanels')['44'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['44'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q44)
async def answer_q44(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q44'] = answer

    if "yes_no" in file_system.read('interactivePanels')['45'][0]:
        await message.answer(file_system.read('interactivePanels')['45'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['45'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q45)
async def answer_q45(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q45'] = answer

    if "yes_no" in file_system.read('interactivePanels')['46'][0]:
        await message.answer(file_system.read('interactivePanels')['46'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['46'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q46)
async def answer_q46(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q46'] = answer

    if "yes_no" in file_system.read('interactivePanels')['47'][0]:
        await message.answer(file_system.read('interactivePanels')['47'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['47'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q47)
async def answer_q47(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q47'] = answer

    if "yes_no" in file_system.read('interactivePanels')['48'][0]:
        await message.answer(file_system.read('interactivePanels')['48'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['48'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q48)
async def answer_q48(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q48'] = answer

    if "yes_no" in file_system.read('interactivePanels')['49'][0]:
        await message.answer(file_system.read('interactivePanels')['49'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['49'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q49)
async def answer_q49(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q49'] = answer

    if "yes_no" in file_system.read('interactivePanels')['50'][0]:
        await message.answer(file_system.read('interactivePanels')['50'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['50'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q50)
async def answer_q50(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q50'] = answer

    if "yes_no" in file_system.read('interactivePanels')['51'][0]:
        await message.answer(file_system.read('interactivePanels')['51'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['51'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q51)
async def answer_q51(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q51'] = answer

    if "yes_no" in file_system.read('interactivePanels')['52'][0]:
        await message.answer(file_system.read('interactivePanels')['52'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['52'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q52)
async def answer_q52(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q52'] = answer

    if "yes_no" in file_system.read('interactivePanels')['53'][0]:
        await message.answer(file_system.read('interactivePanels')['53'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['53'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q53)
async def answer_q53(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q53'] = answer

    if "yes_no" in file_system.read('interactivePanels')['54'][0]:
        await message.answer(file_system.read('interactivePanels')['54'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['54'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q54)
async def answer_q54(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q54'] = answer

    if "yes_no" in file_system.read('interactivePanels')['55'][0]:
        await message.answer(file_system.read('interactivePanels')['55'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['55'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q55)
async def answer_q55(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q55'] = answer

    if "yes_no" in file_system.read('interactivePanels')['56'][0]:
        await message.answer(file_system.read('interactivePanels')['56'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['56'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q56)
async def answer_q56(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q56'] = answer

    if "yes_no" in file_system.read('interactivePanels')['57'][0]:
        await message.answer(file_system.read('interactivePanels')['57'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['57'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q57)
async def answer_q57(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q57'] = answer

    if "yes_no" in file_system.read('interactivePanels')['58'][0]:
        await message.answer(file_system.read('interactivePanels')['58'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['58'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q58)
async def answer_q58(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q58'] = answer

    if "yes_no" in file_system.read('interactivePanels')['59'][0]:
        await message.answer(file_system.read('interactivePanels')['59'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['59'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q59)
async def answer_q59(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q59'] = answer

    if "yes_no" in file_system.read('interactivePanels')['60'][0]:
        await message.answer(file_system.read('interactivePanels')['60'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['60'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q60)
async def answer_q60(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q60'] = answer

    if "yes_no" in file_system.read('interactivePanels')['61'][0]:
        await message.answer(file_system.read('interactivePanels')['61'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['61'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()

@dp.message_handler(state=InteractivePanels.Q61)
async def answer_q61(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q61'] = answer

    if "yes_no" in file_system.read('interactivePanels')['62'][0]:
        await message.answer(file_system.read('interactivePanels')['62'][1], reply_markup=yes_no)
    else:
        await message.answer(file_system.read('interactivePanels')['62'][1], reply_markup=ReplyKeyboardRemove())

    await InteractivePanels.next()



@dp.message_handler(state=InteractivePanels.End)
async def end_test(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['Q68'] = answer

    data = await state.get_data()
    print(data)

    await message.answer(f"Экспертиза панели с серийным номером {data['serial']} завершена\n"
                            "Для проведения экспертизы другой интерактивной панели выберите команду /test",  reply_markup=ReplyKeyboardRemove())

    await state.finish()
