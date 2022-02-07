from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from utils import file_system, utilities
from loader import dp
from backend_4me import get_services, get_service_instance, get_subject
from logging import log, INFO


class Request(StatesGroup):
    Service = State()
    Service_instance = State()
    Subject = State()
    Comment = State()
    Send = State()


@dp.message_handler(commands=["request"])
async def start_request(message: types.Message):
    if str(message.from_user.id) not in file_system.read("users"):
        await message.reply("Вы не авторизованы. Для авторизации выберите команду: /auth")
        log(INFO, f"Non-Auth attempt to create response. userid[{message.from_user.id}]")
    else:
        log(INFO, f"Starting create response. userid[{message.from_user.id}]")
        buttons = get_services()
        service_keyboard = utilities.make_keyboard(buttons)
        await message.reply("Выберите услугу:", reply_markup=service_keyboard)
        await Request.Service.set()


@dp.message_handler(state=Request.Service)
async def request_service(message: types.Message, state: FSMContext):
    if message.text in get_services().values():
        log(INFO, f"user_id[{message.from_user.id}] choose [{message.text}]")
        async with state.proxy() as data:
            data["id_s"] = utilities.get_key(get_services(), message.text)
        buttons = get_service_instance(utilities.get_key(get_services(), message.text))
        instances_keyboard = utilities.make_keyboard(buttons)
        await message.reply("Выберите компонент услуги:", reply_markup=instances_keyboard)
        await Request.Service_instance.set()
    else:
        # TODO: Сделать ввод темы обращения
        return await message.reply("Неверный формат ввода. Введите тему обращения.")


@dp.message_handler(state=Request.Service_instance)
async def request_service_instance(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text in get_service_instance(data["id_s"]).values():
        log(INFO, f"user_id[{message.from_user.id}] choose [{message.text}]")
        async with state.proxy() as data:
            data["id_si"] = utilities.get_key(get_service_instance(data["id_s"]), message.text)
        buttons = get_subject(data["id_s"])
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


@dp.message_handler(state=Request.Comment)
async def request_comment(message: types.Message, state: FSMContext):
    log(INFO, f"user_id[{message.from_user.id}] comment: {message.text}")
    async with state.proxy() as data:
        data["comment"] = message.text
    await message.reply("Проверьте данные вашего запроса перед отправкой:", reply_markup=types.ReplyKeyboardRemove())
    await Request.Send.set()


@dp.message_handler(state=Request.Send)
async def request_send(message: types.Message, state: FSMContext):
    if message.text == "Отправить":
        log(INFO, f"user_id[{message.from_user.id}] send request.")
        data = await state.get_data()
        print(data)