from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from utils import file_system
from loader import dp
from states.interactivePanels import InteractivePanels


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    # await Form.ip[0].set()

    await message.reply("Hello")


# You can use state '*' if you need to handle all states
# @dp.message_handler(lambda message: message.text.lower() == 'cancel', state='*')
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    # if raw_state is None:
    #     return

    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Canceled.', reply_markup=types.ReplyKeyboardRemove())

# for i in range(len(Form.ip)):
# @dp.message_handler(state=Form.ip)
# async def process_name(message: types.Message, state: FSMContext):
#     """
#     Process user name
#     """
#     # async with state.proxy() as data:
#     #     data['name'] = message.text
#     # current_state = await state.get_state()
#     # print(current_state)
#
#     await Form.next()
#     await message.reply("file_system.read('interactivePanels')[str(i)]")
#
#
# # Check age. Age gotta be digit
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
# async def failed_process_age(message: types.Message):
#     """
#     If age is invalid
#     """
#     return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")
#
#
# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     # Update state and data
#     await Form.next()
#     await state.update_data(age=int(message.text))
#
#     # Configure ReplyKeyboardMarkup
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     markup.add("Male", "Female")
#     markup.add("Other")
#
#     await message.reply("What is your gender?", reply_markup=markup)
#
#
# @dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
# async def failed_process_gender(message: types.Message):
#     """
#     In this example gender has to be one of: Male, Female, Other.
#     """
#     return await message.reply("Bad gender name. Choose you gender from keyboard.")
#
#
# @dp.message_handler(state=Form.gender)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gender'] = message.text
#         print(data)
#
#         # Remove keyboard
#         markup = types.ReplyKeyboardRemove()
#
#         # And send message
#         await bot.send_message(message.chat.id, md.text(
#             md.text('Hi! Nice to meet you,', md.bold(data['name'])),
#             md.text('Age:', data['age']),
#             md.text('Gender:', data['gender']),
#             sep='\n'), reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
#
#         # Finish conversation
#         data.state = None


if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=True)
