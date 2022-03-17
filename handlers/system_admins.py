from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import Command

from admincheck import AdminCheck
from loader import dp


@dp.message_handler(Command("admin"), AdminCheck())
async def admin_start(message: types.Message):
    await message.reply("Вы в меню администратора")
    log(INFO, f"Open admin menu. userid[{message.from_user.id}]")
    return



