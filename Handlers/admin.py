from aiogram import types, Dispatcher
from config import bot, ADMINS

async def ban(message: types.Message):
    if message.chat.type !="private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС")
        elif not message.reply_to_message:
            await message.answer("Укажи кого банить")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} banned '
                                 f'{message.reply_to_message.from_user.full_name}')
    else:
        await message.answer("Пиши в группе")


async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Укажи какое сообщение закрепить")
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id, message.reply_to_message)


def register_handlers_admins(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="!/")