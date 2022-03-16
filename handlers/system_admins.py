from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import Command

import utilities
from backend_4me import check_admin
from loader import dp


@dp.message_handler(Command("admin"))
async def admin_start(message: types.Message):
    id4me = utilities.get_id_from_telegram(message.from_user.id)
    answer = await check_admin(id4me)
    teams = []
    team_names = []
    for team in answer:
        teams.append(team['id'])
        team_names.append(team['name'])
    if not teams:
        log(INFO, f"user_id[{message.from_user.id}] push admin, не входит в техподдержку")
        await message.answer("Вы не входите в команды техподдержки")
    elif teams:
        log(INFO, f"user_id[{message.from_user.id}] push admin, входит в техподдержку [{teams}]")
        msg = ''
        for team_name in team_names:
            msg += team_name + '\n'
        await message.answer("Вы входите в команды:\n" + msg)

