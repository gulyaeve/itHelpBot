from config import bot_admin
from loader import bot, storage, dp
from utils.utilities import set_default_commands, notify_admins
import filters, middlewares, handlers
from aiogram import executor


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


async def on_startup(dp):
    await set_default_commands(dp)
    await notify_admins(bot_admin)


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
