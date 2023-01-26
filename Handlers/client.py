from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import start_markup

# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салалекум хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method")
    # await message.reply("This is a reply method")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)
    question = "Invoker or Shadow fiend?"
    answers = [
        "Invoker",
        "Shadow fiend"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="1000-7",
        open_period=60,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/mem.png", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
