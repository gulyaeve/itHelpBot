from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    # await Form.ip[0].set()

    await message.reply("Добро пожаловать в чат-бот техподдержки!")


# You can use state '*' if you need to handle all states
# @dp.message_handler(lambda message: message.text.lower() == 'cancel', state='*')
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    await state.finish()
    await message.reply('Действие отменено.', reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=True)
