from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import db


class Get4me(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        user = await db.select_user(telegram_id=message.from_user.id)
        if user is not None:
            if user["full_name"] != message.from_user.full_name:
                await db.update_user_fullname(message.from_user.full_name, message.from_user.id)
                log(INFO, f"Updated full_name [{message.from_user.full_name}] for [{message.from_user.id}]")
            if user["username"] != message.from_user.username:
                await db.update_user_username(message.from_user.username, message.from_user.id)
                log(INFO, f"Updated username [{message.from_user.username}] for [{message.from_user.id}]")
        else:
            await db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
            log(INFO, f"Added user to db [{message.from_user.id}] [{message.from_user.username}] [{message.from_user.full_name}]")

    async def on_process_message(self, message: types.Message, data: dict):
        user = await db.select_user(telegram_id=message.from_user.id)
        if user is not None:
            data["id4me"] = str(user["id4me"])
            log(INFO, f"Middleware get id4me [{data['id4me']}] for [{message.from_user.id}]")
