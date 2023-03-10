import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.backend_4me import FourMe
from config import telegram_token, proxy_url
from utils.db_api.postgresql import Database

if proxy_url:
    bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML, proxy=proxy_url)
else:
    bot = Bot(token=telegram_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
fourme = FourMe()
logging.basicConfig(handlers=(logging.FileHandler('logs/log.txt'), logging.StreamHandler()),
                    format=u'%(asctime)s %(filename)s [LINE:%(lineno)d] #%(levelname)-15s %(message)s',
                    level=logging.INFO,
                    )
