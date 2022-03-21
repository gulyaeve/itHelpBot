from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils import file_system


class AuthCheck(BoundFilter):
    async def check(self, message: types.Message):
        log(INFO, f"{message.from_user.id}: {str(message.from_user.id) in file_system.read('users')}")
        return str(message.from_user.id) in file_system.read("users")

