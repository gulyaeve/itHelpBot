from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from re import match
from utils import file_system
from loader import dp
from send_email import send_email
from backend_4me import get_id
from random import randrange
from logging import log, INFO
from filters import AuthCheck

email_pattern = r"^[a-zA-Z0-9._%+-]+[@]+[a-zA-Z0-9._%+-]*mos.ru$"


class Auth(StatesGroup):
    Email = State()
    Code = State()


@dp.message_handler(AuthCheck(), commands=["logout"])
async def cmd_logout(message: types.Message):
    log(msg=f"Logout user_id[{message.from_user.id}], username[{message.from_user.username}]",
        level=INFO)
    file_system.delete_user(str(message.from_user.id))
    await message.reply("Вы успешно деавторизованы!")


@dp.message_handler(AuthCheck(), commands=["auth"])
async def cmd_auth(message: types.Message):
    await message.reply("Вы уже авторизованы!")


@dp.message_handler(commands=["auth"])
async def cmd_auth(message: types.Message):
    log(msg=f"Start authentication for user_id[{message.from_user.id}], username[{message.from_user.username}]",
        level=INFO)
    await message.reply("Введите ваш e-mail, связанный с СУДИР:")
    await Auth.Email.set()


@dp.message_handler(state=Auth.Email)
async def enter_code(message: types.Message, state: FSMContext):
    email = message.text
    if match(email_pattern, message.text):
        id4me = await get_id(email)
        if id4me == 0:
            log(msg=f"Invalid email[{email}]; user_id[{message.from_user.id}]", level=INFO)
            await message.answer("Пользователь не найден.")
            await state.finish()
        else:
            code = randrange(1, 10 ** 6)
            log(msg=f"Generate code[{code}]; id4me[{id4me}]; email[{email}]; user_id[{message.from_user.id}]",
                level=INFO)
            await send_email(email, f"Здраствуйте! Ваш код подтверждения: {code}")
            await message.answer("На ваш e-mail отправлен код подтверждения. Введите код подтверждения из письма:")
            async with state.proxy() as data:
                data["email"] = email
                data["id4me"] = id4me
                data["code"] = code
            await Auth.Code.set()
    else:
        log(msg=f"Wrong email[{email}]; user_id[{message.from_user.id}]", level=INFO)
        return await message.answer(
            "Неверный формат ввода. Введите корректный адрес электронной почты.")


@dp.message_handler(state=Auth.Code)
async def code_confirm(message: types.Message, state: FSMContext):
    telegram_id = str(message.from_user.id)
    data = await state.get_data()
    if message.text == str(data["code"]):
        log(msg=f"Enter valid code[{message.text}]; user_id[{message.from_user.id}]", level=INFO)
        file_system.new_user(message.from_user.id)
        file_system.update_user(telegram_id, "email", data["email"])
        file_system.update_user(telegram_id, "id4me", data["id4me"])
        log(msg=f"Пользователь сохранён id[{telegram_id}]; email[{data['email']}]; id4me[{data['id4me']}]",
            level=INFO)
        await message.answer("Вы успешно авторизовались! Для выхода введите команду: /logout")
        await state.finish()
    else:
        log(msg=f"Enter wrong code[{message.text}]; user_id[{message.from_user.id}]", level=INFO)
        return await message.answer("Введён неверный код подтверждения.")
