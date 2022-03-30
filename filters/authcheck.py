from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db
from utils import file_system


class AuthCheck(BoundFilter):
    async def check(self, message: types.Message):
        user = await db.select_user(telegram_id=message.from_user.id)
        if user is None:
            return False
        else:
            return True
        # log(INFO, f"{message.from_user.id}: {str(message.from_user.id) in file_system.read('users')}")
        # return str(message.from_user.id) in file_system.read("users")

