from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import utilities
from utils import file_system


class Get4me(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user = message.from_user.id
        if str(user) in file_system.read("users"):
            id4me = utilities.get_id_from_telegram(user)
            data["id4me"] = str(id4me)
            log(INFO, f"[{user}] [{data=}]")
