from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from filters import AuthCheck
from keyboards import keyboards

from utils import utilities
from loader import dp
from backend_4me import get_services, get_service_instance, get_subject, send_request
from logging import log, INFO


class Request(StatesGroup):
    Service = State()
    Service_instance = State()
    Subject = State()
    Comment = State()
    Send = State()


@dp.message_handler(AuthCheck(), commands=["request"])
async def start_request(message: types.Message):
    log(INFO, f"userid[{message.from_user.id}] Starting create response")
    buttons = await get_services()
    service_keyboard = utilities.make_keyboard(buttons)
    await message.reply("Выберите услугу", reply_markup=service_keyboard)
    await Request.Service.set()


@dp.message_handler(commands=["request"])
async def start_request_non_auth(message: types.Message):
    await message.reply("Вы не авторизованы. Для авторизации выберите команду: /auth")
    log(INFO, f"Non-Auth attempt to create response. userid[{message.from_user.id}]")
    return


@dp.message_handler(state=Request.Service)
async def request_service(message: types.Message, state: FSMContext, id4me):
    services = await get_services()
    if message.text in services.values():
        log(INFO, f"user_id[{message.from_user.id}] choose [{message.text}]")
        async with state.proxy() as data:
            data["id4me"] = id4me
            data["id_s"] = utilities.get_key(services, message.text)
        buttons = await get_service_instance(utilities.get_key(services, message.text))
        instances_keyboard = utilities.make_keyboard(buttons)
        await message.reply("Выберите компонент услуги:", reply_markup=instances_keyboard)
        await Request.Service_instance.set()
    else:
        return await message.reply("Неверный формат ввода.")


@dp.message_handler(state=Request.Service_instance)
async def request_service_instance(message: types.Message, state: FSMContext):
    data = await state.get_data()
    service_instance = await get_service_instance(data["id_s"])
    if message.text in service_instance.values():
        log(INFO, f"user_id[{message.from_user.id}] choose [{message.text}]")
        async with state.proxy() as data:
            data["id_si"] = utilities.get_key(service_instance, message.text)
        buttons = await get_subject(data["id_s"])
        subject_keyboard = utilities.make_keyboard(buttons)
        await message.reply("Выберите тему:", reply_markup=subject_keyboard)
        await Request.Subject.set()


@dp.message_handler(state=Request.Subject)
async def request_subject(message: types.Message, state: FSMContext):
    log(INFO, f"user_id[{message.from_user.id}] subject: {message.text}")
    async with state.proxy() as data:
        data["subject"] = message.text
    await message.reply("Введите комментарий для техподдержки:", reply_markup=types.ReplyKeyboardRemove())
    await Request.Comment.set()


@dp.message_handler(state=Request.Comment, content_types=types.ContentType.TEXT)
async def request_comment(message: types.Message, state: FSMContext):
    log(INFO, f"user_id[{message.from_user.id}] comment: {message.text}")
    async with state.proxy() as data:
        data["comment"] = message.text
    await message.reply("Проверьте данные вашего запроса перед отправкой:")
    data = await state.get_data()
    await message.answer(f"Тема запроса: {data['subject']}\n"
                         f"Комментарий: {data['comment']}", reply_markup=keyboards.request_submit)
    await Request.Send.set()


@dp.message_handler(state=Request.Comment, content_types=types.ContentType.ANY)
async def request_comment_nonetext(message: types.Message):
    log(INFO, f"user_id[{message.from_user.id}] comment: {message.text}")
    return await message.reply("Введите комментарий в текстовом формате:")


@dp.message_handler(state=Request.Send)
async def request_send(message: types.Message, state: FSMContext):
    if message.text == "Отправить":
        data = await state.get_data()
        answer = await send_request(data["id4me"], data["subject"], data["comment"], data["id_si"])
        log(INFO, f"Пользователь [{message.from_user.id}] создал запрос:")
        log(INFO, f"{answer}")
        await message.answer(f"Запрос успешно отправлен!", reply_markup=types.ReplyKeyboardRemove())
        try:
            log(INFO, f"Пользователь [{message.from_user.id}] создал запрос #[{answer['id']}]")
            await message.answer(f"Запросу присвоен номер: <code>{answer['id']}</code>")
        except Exception as e:
            log(INFO, f"Пользователь [{message.from_user.id}] создал запрос с ошибкой: {Exception}: {e}")
        await state.finish()
    else:
        return await message.reply("Выберите действие на клавиатуре.")
