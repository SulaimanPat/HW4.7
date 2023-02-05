from aiogram import *
from config import *
from pytube import YouTube
import os

async def start_yt_video(message: types.Message):
    chat_id=message.chat.id
    await bot.send_message(chat_id, "Hello I can download any video from Youtube\n"
                                 "Send me a link")

async def text_message(message: types.Message):
    chat_id=message.chat.id
    url=message.text
    yt=YouTube(url)
    if message.text.startswith=="https:/youtu.be/ or https://www.youtube.com/":
        await bot.send_message(chat_id, f"Downloading video: *{yt.title}*\n"
                                        f"*Author*: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
        await download_yt_video(url, message, bot)

async def download_yt_video(url, message, bot):
    yt=YouTube(url)
    stream=yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f"{message.chat.id}", f"{message.chat.id}_{yt.title}")
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption="*Here is your video*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")

def register_handlers_yt_video(dp: Dispatcher):
    dp.register_message_handler(start_yt_video, commands='dwvideo')
    dp.register_message_handler(text_message)
    dp.register_message_handler(download_yt_video)