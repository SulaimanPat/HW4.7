import random
from aiogram import types, Dispatcher
from config import bot, dp
from random import choice


# @dp.message_handler()




async def echo(message: types.Message):
    if message.text=="game":
        emoji_list=['🎯','🏀', '⚽', '🎳', '🎰']
        await bot.send_dice(message.chat.id, emoji=choice(emoji_list))

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
