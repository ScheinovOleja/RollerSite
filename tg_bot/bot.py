import os
from asyncio.log import logger
from aiogram import Dispatcher
from aiogram.utils import executor
from django.conf import settings

from tg_bot import dp, loop
from tg_bot.handlers import register_chat_viber, register_back_call, register_registration, register_all_message


async def register_handler_chat(dispatcher: Dispatcher):
    register_chat_viber(dispatcher)


async def register_handler_back_call(dispatcher: Dispatcher):
    register_back_call(dispatcher)


async def register_handler_registration(dispatcher: Dispatcher):
    register_registration(dispatcher)


async def register_message_handler(dispatcher: Dispatcher):
    register_all_message(dispatcher)


async def main(dispatcher: Dispatcher):
    await register_handler_chat(dispatcher)
    await register_handler_back_call(dispatcher)
    await register_handler_registration(dispatcher)
    await register_message_handler(dispatcher)


async def shutdown(dispatcher: Dispatcher):
    logger.error(f"Shutdowning...")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RollerSiteCms.settings')
    executor.start_polling(dp, skip_updates=True, loop=loop, on_shutdown=shutdown, on_startup=main)
