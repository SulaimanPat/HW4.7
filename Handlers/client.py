from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import bot
from keyboards.client_kb import start_markup
from parcer.news import parser
from parcer.cybersports import parser

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


async def get_news(message: types.Message):
    news = parser()
    for i in news:
        await message.answer(
            f"{i['link']}\n\n"
            f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
            f"{i['description']}\n"
            f"{i['date_from_html']}\n",
            parse_mode=ParseMode.HTML
        )

async def get_cyber_news(message: types.Message):
    cyber_news = parser()
    for i in cyber_news:
        await message.answer(
            f"{i['link']}\n\n"
            f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
            f"{i['description']}\n"
            f"{i['date_from_html']}\n",
            parse_mode=ParseMode.HTML
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(get_news, commands=['news'])
    dp.register_message_handler(get_news, commands=['cnews'])
