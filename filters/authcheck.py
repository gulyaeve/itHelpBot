from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils import file_system


class AuthCheck(BoundFilter):
    async def check(self, message: types.Message):
        return str(message.from_user.id) in file_system.read("users")

