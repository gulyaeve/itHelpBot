from aiogram import types


def make_dict(r_json, key_name, value_name):
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
