from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db
# from utils import file_system


class AuthCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            user = await db.select_user(telegram_id=message.from_user.id)
            if user is None:
                log(INFO, f"Пользователь в БД не найден [{message.from_user.id}]")
                return False
            else:
                log(INFO, f"Найдена запись в БД: [{user}]")
                return True
        except Exception as err:
            log(INFO, f"{Exception}: {err} Пользователь не найден.")
            return False
        # log(INFO, f"{message.from_user.id}: {str(message.from_user.id) in file_system.read('users')}")
        # return str(message.from_user.id) in file_system.read("users")

