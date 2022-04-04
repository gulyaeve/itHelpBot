from logging import log, INFO

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Regexp
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot_admin
from loader import dp, bot


@dp.message_handler(Text)
async def text_handler(message: types.Message):
    """
    Any text handler
    """
    log(INFO, f"[{message.from_user.id}] написал: {message.text}")
    await message.answer("ℹ️ Для получения справки по командам чат-бота выберите команду:\n<b>/help</b>")
    inline_keyboard = InlineKeyboardMarkup()
    inline_button = InlineKeyboardButton(text="Ответить", callback_data=f'reply_from_anytext_id={message.from_user.id}')
    inline_keyboard.add(inline_button)
    await bot.send_message(bot_admin,
                           f"[{message.from_user.full_name}; @{message.from_user.username}; {message.from_user.id}] "
                           f"написал:\n\n<i>{message.text}</i>",
                           reply_markup=inline_keyboard)


@dp.callback_query_handler(Regexp('reply_from_anytext_id=([0-9]*)'))
async def answer_to_text(callback: types.CallbackQuery, state: FSMContext):
    reply_user_id = callback.data.split("=")[1]
    async with state.proxy() as data:
        data["reply_user_id"] = reply_user_id
    await callback.message.answer(f"Введите ответ:")
    await state.set_state("ANSWER_TO_ANY_TEXT")


@dp.message_handler(state="ANSWER_TO_ANY_TEXT")
async def send_answer_to_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(data["reply_user_id"], message.text)
    log(INFO, f'Пользователю [{data["reply_user_id"]}] отправлено: {message.text}')
    await state.finish()


@dp.message_handler(content_types=ContentType.ANY)
async def content_handler(message: types.Message):
    """
    Any content handler
    """
    log(INFO, f"[{message.from_user.id}] отправил: {message.content_type}")
    await message.answer("ℹ️ Для получения справки по командам чат-бота выберите команду:\n<b>/help</b>")
    await bot.send_message(bot_admin,
                           f"[{message.from_user.full_name}; @{message.from_user.username}; {message.from_user.id}]"
                           f" отправил: {message.content_type}")
    await message.forward(bot_admin)
