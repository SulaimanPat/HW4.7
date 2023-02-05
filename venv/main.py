from aiogram.utils import executor
import logging
from config import dp
from Handlers import client, callback, admin, extra, fsm_anketa, fsmAdminMentor, notifications, download_video
from Database.mentors_db import sq_create

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admins(dp)
fsm_anketa.register_handlers_anketa(dp)
fsmAdminMentor.register_handlers_admin_anketa(dp)
notifications.register_handlers_notification(dp)
download_video.register_handlers_yt_video(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)