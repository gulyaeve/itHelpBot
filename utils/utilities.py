from logging import log, INFO

from aiogram import types

from config import bot_admin
# from utils import file_system
from loader import bot
import re


async def set_default_commands():
    return await bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать работу с ботом"),
        types.BotCommand(command="/auth", description="Авторизация"),
        types.BotCommand(command="/request", description="Отправить заявку"),
        types.BotCommand(command="/logout", description="Деавторизация"),
    ])


async def notify_admins(message):
    try:
        await bot.send_message(bot_admin, message)
    except:
        log(INFO, f"Admin [{bot_admin}] block this bot")


async def make_dict(r_json, key_name, value_name):
    keys = []
    values = []
    for item in r_json:
        for attribute, value in item.items():
            if attribute == key_name:
                keys.append(value)
            if attribute == value_name:
                values.append(value)
    return dict(zip(keys, values))


def get_key(d: dict, value):
    for k, v in d.items():
        if v == value:
            return k


def make_keyboard(buttons: dict):
    keyboard = types.ReplyKeyboardMarkup()
    for button in buttons.values():
        keyboard.add(button)
    keyboard.add("ОТМЕНА")
    return keyboard


# def get_id_from_telegram(user_id):
#     return file_system.read("users")[str(user_id)]["id4me"]


# def get_telegram_from_id(id4me):
#     telegram_id = ''
#     for user_id in file_system.read("users"):
#         if file_system.read("users")[user_id]["id4me"] == id4me:
#             telegram_id = str(user_id)
#     return telegram_id


def make_text(input_text):
    return re.sub(r'<.*?>', '', input_text)
