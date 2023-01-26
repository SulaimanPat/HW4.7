from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next', callback_data='button_call_2')
    markup.add(button_call_2)
    question = "Blink Eul ult+?"
    answers = [
        'F9',
        'destroy items']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="U missed timing",
        open_period=60,
        reply_markup=markup

    )

async def quiz_3(call: types.CallbackQuery):
    question = "Bkb or Arcane blink?"
    answers = [
        'Bkb',
        'Arcane blink']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Bkb for pussies",
        open_period=60,
    )
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")