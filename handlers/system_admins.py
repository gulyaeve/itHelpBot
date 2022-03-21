from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from backend_4me import check_admin, get_requests_for_team, get_requests_for_member, get_request, get_notes_for_request
from filters import AdminCheck
from loader import dp, bot
from utils.utilities import make_text


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
        inline_button = InlineKeyboardButton(text=text, callback_data=request["id"])
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


@dp.callback_query_handler(AdminCheck())
async def get_request_info(callback: types.CallbackQuery):
    request_id = callback.data
    request = await get_request(request_id)
    notes = await get_notes_for_request(request_id)
    report = f'<b>Тема:</b> {request["subject"]}\n' \
             f'<b>Автор:</b> {request["requested_by"]["name"]}\n' \
             f'<b>Время создания:</b> {request["created_at"].replace("T", " ").split("+")[0]}\n' \
             f'<b>Целевое время решения:</b> {request["resolution_target_at"].replace("T", " ").split("+")[0]}\n\n'
    for note in notes:
        report += f"<i>{make_text(note['text'])}\n\n</i>"
    await bot.send_message(callback.from_user.id, f"{report}")
