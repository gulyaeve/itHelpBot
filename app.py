from loader import bot, storage, dp
from utils.utilities import set_default_commands
import filters, middlewares, handlers
from aiogram import executor


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':

    # from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=set_default_commands)
