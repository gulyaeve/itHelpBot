import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

from utils import file_system
from loader import dp
from send_email import send_email
from backend_4me import get_id

email_pattern = r"^([\w-]+(?:\.[\w-]+)*)+[@](edu.mos.ru)"


class Auth(StatesGroup):
    Email = State()
    Code = State()


@dp.message_handler(commands=["auth"])
async def cmd_auth(message: types.Message):
    await message.reply("Вы Введите ваш e-mail, связанный с СУДИР:")
    await Auth.Email.set()


@dp.message_handler(state=Auth.Email)
async def enter_code(message: types.Message, state: FSMContext):
    if re.match(email_pattern, message.text):
        email = message.text
        id4me = get_id(email)
        send_email(email, f"Hello! Your id in 4me: {id4me}")
        await message.answer("На ваш e-mail отправлен код подтверждения. Введите код подтверждения из письма:")
        async with state.proxy() as data:
            data["email"] = email
            data["id4me"] = id4me
        await Auth.Code.set()
    else:
        return await message.answer(
            "Неверный формат ввода. Введите корректный адрес электронной почты.")


@dp.message_handler(state=Auth.Code)
async def code_confirm(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == str(data["id4me"]):
        # TODO: Сделать сохранение telegram_id в 4me
        await message.answer("Вы успешно авторизовались!")
        await state.finish()
    else:
        return await message.answer("Введён неверный код подтверждения.")
