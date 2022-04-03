from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from logging import log, INFO
from filters import AuthCheck, AdminCheck

from backend_4me import check_admin
from loader import dp


@dp.message_handler(AdminCheck(), commands=['start'])
async def cmd_start_admin(message: types.Message, id4me):
    log(INFO, f"ADMIN [{message.from_user.id}] нажал START.")
    await message.reply("Добро пожаловать в чат-бот техподдержки! 🧰 💻")
    await message.answer("🔧 Для создания запроса на техподдержку выберите команду: /request")
    answer = await check_admin(id4me)
    teams = []
    team_names = []
    for team in answer:
        teams.append(team['id'])
        team_names.append(team['name'])
    if teams:
        log(INFO, f"user_id[{message.from_user.id}] push start, входит в техподдержку [{teams}]")
        msg = ''
        for team_name in team_names:
            msg += team_name + '\n'
        await message.answer("🛠 Вы входите в команды:\n" + msg + "Для просмотра заявок, назначенных вам: /admin")


@dp.message_handler(AuthCheck(), commands=['start'])
async def cmd_start_user(message: types.Message, id4me):
    """
    Conversation's entry point
    """
    log(INFO, f"USER [{message.from_user.id}] нажал START.")
    await message.reply("Добро пожаловать в чат-бот техподдержки! 🧰 💻")
    await message.answer("🔧 Для создания запроса на техподдержку выберите команду: /request")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    log(INFO, f"USER WITHOUT AUTH [{message.from_user.id}] нажал START.")
    await message.reply("Добро пожаловать в чат-бот техподдержки! 🧰 💻")
    await message.answer("👤 Для работы с ботом пройдите авторизацию по команде: /auth")


# You can use state '*' if you need to handle all states
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    log(INFO, f"[{message.from_user.id}] отменил действие.")
    await state.finish()
    await message.reply('Действие отменено.', reply_markup=types.ReplyKeyboardRemove())
