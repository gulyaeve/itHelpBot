from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils import utilities
from backend_4me import check_admin


class AdminCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            id4me = utilities.get_id_from_telegram(message.from_user.id)
            answer = await check_admin(id4me)
            if answer:
                return True
            else:
                return False
        except Exception as err:
            log(INFO, f"{Exception}: {err} Пользователь не найден.")
            return False


