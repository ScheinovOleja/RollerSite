import os
import sys

sys.path.append('/root/RollerSite/')

from asyncio.log import logger

from aiogram import Dispatcher
from aiogram.utils import executor

from tg_bot import dp, loop
from tg_bot.handlers import register_registration, register_all_message, \
    register_reviews

async def register_handler_registration(dispatcher: Dispatcher):
    register_registration(dispatcher)


async def register_message_handler(dispatcher: Dispatcher):
    register_all_message(dispatcher)


async def register_reviews_handler(dispatcher: Dispatcher):
    register_reviews(dispatcher)


async def main(dispatcher: Dispatcher):
    await register_reviews_handler(dispatcher)
    await register_handler_registration(dispatcher)
    await register_message_handler(dispatcher)


async def shutdown(dispatcher: Dispatcher):
    logger.error(f"Shutdowning...")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RollerSiteCms.settings')
    executor.start_polling(dp, skip_updates=True, loop=loop, on_shutdown=shutdown, on_startup=main)
