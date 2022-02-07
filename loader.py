import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import telegram_token

bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] [%(funcName)s()] #%(levelname)-5s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )


async def set_default_commands(dp):
    return await bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать работу с ботом"),
        types.BotCommand(command="/auth", description="Авторизоваться в 4me"),
        types.BotCommand(command="/request", description="Отправить заявку")
    ])
