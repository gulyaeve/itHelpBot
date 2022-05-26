from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from re import match
from loader import dp, db, fourme
from send_email import send_email
# from backend_4me import get_id
from random import randrange
from logging import log, INFO
from filters import AuthCheck

email_pattern = r"^[a-zA-Z0-9._%+-]+[@]+[a-zA-Z0-9._%+-]*mos.ru$"


class Auth(StatesGroup):
    Email = State()
    Code = State()


@dp.message_handler(AuthCheck(), commands=["auth"])
async def cmd_auth(message: types.Message):
    await message.reply("Вы уже авторизованы!")


@dp.message_handler(commands=["auth"])
async def cmd_auth_all(message: types.Message):
    log(msg=f"Start authentication for user_id[{message.from_user.id}], username[{message.from_user.username}]",
        level=INFO)
    await message.reply("Введите ваш e-mail:")
    await Auth.Email.set()


@dp.message_handler(state=Auth.Email)
async def enter_code(message: types.Message, state: FSMContext):
    email = message.text
    if match(email_pattern, message.text):
        id4me = await fourme.get_id(email)
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
    data = await state.get_data()
    if message.text == str(data["code"]):
        log(msg=f"Enter valid code[{message.text}]; user_id[{message.from_user.id}]", level=INFO)
        await db.update_user_email(message.from_user.id, data['email'])
        await db.update_user_id4me(message.from_user.id, data["id4me"])
        user = await db.select_user(telegram_id=message.from_user.id)
        log(INFO, f"Success update in DB: {user}")
        await message.answer("Вы успешно авторизовались!\n"
                             "Для подачи заявки на техподдержку воспользуйтесь командой:\n<b>/request</b>")
        await state.finish()
    else:
        log(msg=f"Enter wrong code[{message.text}]; user_id[{message.from_user.id}]", level=INFO)
        return await message.answer("Введён неверный код подтверждения.")
