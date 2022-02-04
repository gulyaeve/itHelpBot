import re
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State

from utils import file_system
from loader import dp
from send_email import send_email
from backend_4me import get_id
from random import randrange

email_pattern = r"^([\w-]+(?:\.[\w-]+)*)+[@](edu.mos.ru)"


class Auth(StatesGroup):
    Email = State()
    Code = State()


@dp.message_handler(commands=["auth"])
async def cmd_auth(message: types.Message):
    logging.log(msg=f"Start authentication for user_id[{message.from_user.id}], username[{message.from_user.username}]",
                level=logging.INFO)
    await message.reply("Введите ваш e-mail, связанный с СУДИР:")
    await Auth.Email.set()


@dp.message_handler(state=Auth.Email)
async def enter_code(message: types.Message, state: FSMContext):
    email = message.text
    if re.match(email_pattern, message.text):
        id4me = get_id(email)
        if id4me == 0:
            logging.log(msg=f"Invalid email[{email}]; user_id[{message.from_user.id}]", level=logging.INFO)
            await message.answer("Пользователь не найден.")
            await state.finish()
        else:
            code = randrange(1, 10**6)
            send_email(email, f"Здраствуйте! Ваш код подтверждения: {code}")
            await message.answer("На ваш e-mail отправлен код подтверждения. Введите код подтверждения из письма:")
            async with state.proxy() as data:
                data["email"] = email
                data["id4me"] = id4me
                data["code"] = code
            logging.log(msg=f"Generate code[{code}]; id4me[{id4me}]; email[{email}]; user_id[{message.from_user.id}]",
                        level=logging.INFO)
            await Auth.Code.set()
    else:
        logging.log(msg=f"Wrong email[{email}]; user_id[{message.from_user.id}]", level=logging.INFO)
        return await message.answer(
            "Неверный формат ввода. Введите корректный адрес электронной почты.")


@dp.message_handler(state=Auth.Code)
async def code_confirm(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == str(data["code"]):
        logging.log(msg=f"Enter valid code[{message.text}]; user_id[{message.from_user.id}]", level=logging.INFO)
        # TODO: Сделать сохранение telegram_id в 4me
        await message.answer("Вы успешно авторизовались!")
        await state.finish()
    else:
        logging.log(msg=f"Enter wrong code[{message.text}]; user_id[{message.from_user.id}]", level=logging.INFO)
        return await message.answer("Введён неверный код подтверждения.")
