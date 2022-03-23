from logging import log, INFO

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(Text)
async def text_handler(message: types.Message):
    """
    Any text handler
    """
    log(INFO, f"[{message.from_user.id}] написал: {message.text}")


@dp.message_handler(content_types=ContentType.ANY)
async def content_handler(message: types.Message):
    """
    Any content handler
    """
    log(INFO, f"[{message.from_user.id}] отправил: {message.content_type}")