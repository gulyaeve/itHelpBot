from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards import keyboards
from loader import dp, db
from logging import log, INFO
from filters import AuthCheck


@dp.message_handler(AuthCheck(), commands=["logout"])
async def cmd_logout_auth(message: types.Message, state: FSMContext):
    await message.reply("Вы уверены?", reply_markup=keyboards.yes_no)
    await state.set_state("confirm")


@dp.message_handler(commands=["logout"])
async def cmd_logout_all(message: types.Message):
    await message.reply("Вы ещё не авторизованы. Для авторизации выберите команду: <b>/auth</b>")


@dp.message_handler(Text(equals="да", ignore_case=True), state="confirm")
async def logout_yes(message: types.Message, state: FSMContext):
    log(INFO, f"Logout user_id[{message.from_user.id}], username[{message.from_user.username}]")
    await db.delete_user(message.from_user.id)
    await message.reply("Вы успешно деавторизованы!"
                        "Для повторной авторизации выберите команду: <b>/auth</b>",
                        reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals="нет", ignore_case=True), state="confirm")
async def logout_no(message: types.Message, state: FSMContext):
    await message.reply("Деавторизация отменена.", reply_markup=ReplyKeyboardRemove())
    await state.finish()
