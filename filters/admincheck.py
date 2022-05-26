from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db, fourme


class AdminCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            # id4me = utilities.get_id_from_telegram(message.from_user.id)
            user = await db.select_user(telegram_id=message.from_user.id)
            if user["id4me"] is not None:
                answer = await fourme.check_admin(user["id4me"])
                if answer:
                    log(INFO, f"Пользователь [{message.from_user.id}] входит в техподдержку.")
                    return True
                else:
                    log(INFO, f"Команды техподдержки для пользователя [{message.from_user.id}] не найдены.")
                    return False
            else:
                return False
        except:
            return False


