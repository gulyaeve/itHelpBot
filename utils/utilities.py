from aiogram import types
from utils import file_system
from loader import bot


async def set_default_commands(dp):
    return await bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать работу с ботом"),
        types.BotCommand(command="/auth", description="Авторизоваться в 4me"),
        types.BotCommand(command="/request", description="Отправить заявку")
    ])


async def notify_admins(bot_admin):
    await bot.send_message(bot_admin, "Бот запущен и готов к работе.")


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


def get_id_from_telegram(user_id):
    return file_system.read("users")[str(user_id)]["id4me"]
