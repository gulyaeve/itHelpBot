from logging import log, INFO

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from backend_4me import get_requests_for_member, get_request, get_notes_for_request, post_note_to_request
from filters import AdminCheck
from loader import dp, bot
from utils.utilities import make_text, get_telegram_from_id


class Action(StatesGroup):
    Reply = State()
    Close = State()


@dp.message_handler(Command("admin"), AdminCheck())
async def admin_start(message: types.Message, id4me):
    log(INFO, f"Open admin menu. userid[{message.from_user.id}]")
    answer = await get_requests_for_member(id4me)
    if not answer:
        await message.answer("В настоящий момент вам не назначены запросы.")
        return
    inline_keyboard = InlineKeyboardMarkup()
    for request in answer:
        text = str(request["id"]) + ": " + request["subject"]
        inline_button = InlineKeyboardButton(text=text, callback_data=f'request_id={request["id"]}')
        inline_keyboard.add(inline_button)
    await message.answer(f"Запросы для вас:", reply_markup=inline_keyboard)

    # await message.reply("Вы в меню администратора")
    # log(INFO, f"Open admin menu. userid[{message.from_user.id}]")
    # answer = await check_admin(id4me)
    # for team in answer:
    #     team_id = team['id']
    #     team_name = team["name"]
    #     inline_keyboard = InlineKeyboardMarkup()
    #     answer = await get_requests_for_team(team_id)
    #     for request in answer:
    #         text = str(request["id"]) + ": " + request["subject"]
    #         inline_button = InlineKeyboardButton(text=text, callback_data=request["id"])
    #         inline_keyboard.add(inline_button)
    #     await message.answer(f"Запросы для команды {team_name}:", reply_markup=inline_keyboard)


@dp.callback_query_handler(AdminCheck(), Regexp('request_id=([0-9]*)'))
async def get_request_info(callback: types.CallbackQuery):
    request_id = callback.data.split("=")[1]
    request = await get_request(request_id)
    notes = await get_notes_for_request(request_id)
    report = f'<b>Номер заявки:</b> <code>{request["id"]}</code>\n' \
             f'<b>Тема:</b> {request["subject"]}\n' \
             f'<b>Автор:</b> {request["requested_by"]["name"]}\n' \
             f'<b>Время создания:</b> {request["created_at"].replace("T", " ").split("+")[0]}\n' \
             f'<b>Целевое время решения:</b> {request["resolution_target_at"].replace("T", " ").split("+")[0]}\n\n'
    for note in notes:
        report += f"<i>{make_text(note['text'])}\n\n</i>"
    # buttons = [[InlineKeyboardButton("Ответить 💬", callback_data=f"reply={request_id}"),
    #             InlineKeyboardButton("Завершить ✅", callback_data=f"close={request_id}")]]
    buttons = [[InlineKeyboardButton("Ответить 💬", callback_data=f"reply={request_id}")]]
    actions_to_request = InlineKeyboardMarkup(row_width=2, inline_keyboard=buttons)
    await bot.send_message(callback.from_user.id, f"{report}", reply_markup=actions_to_request)


@dp.callback_query_handler(AdminCheck(), Regexp('reply=([0-9]*)'))
async def request_reply(callback: types.CallbackQuery, state: FSMContext):
    request_id = callback.data.split("=")[1]
    async with state.proxy() as data:
        data["request_id"] = request_id
    await callback.message.answer(f"Введите комментарий к заявке №{request_id}:")
    await Action.Reply.set()


@dp.message_handler(AdminCheck(), state=Action.Reply)
async def make_reply_to_request(message: types.Message, state: FSMContext):
    data = await state.get_data()
    request_id = data['request_id']
    text = message.text.replace('\n', ' ') + " (Отправлено из чат-бота https://t.me/itHelpDigitalCenter_bot)"
    answer = await post_note_to_request(request_id, message.text)
    log(INFO, f"ADMIN [{message.from_user.id}] posted note with id [{answer['id']}] to [{request_id}]")
    request = await get_request(request_id)
    id4me_requested_for = request['requested_for']['id']
    telegram_requested_for = get_telegram_from_id(id4me_requested_for)
    if telegram_requested_for:
        try:
            bot.send_message(telegram_requested_for, f"К вашей заявке <code>{request_id}</code> добавлен комментарий:\n"
                                                     f"<i>{text}</i>")
            log(INFO, f"Автору [{telegram_requested_for}] запроса [{request_id}] отправлено уведомление.")
        except:
            pass
    await message.answer(f"Комментарий к заявке №{request_id} отправлен.")
    await state.finish()


