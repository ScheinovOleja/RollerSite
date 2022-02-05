import os
import sys
from asyncio.log import logger

from aiogram import Dispatcher
from aiogram.utils import executor

from tg_bot_private import dp, loop
from tg_bot_private.handlers import register_chat_viber

sys.path.append('/root/RollerSite/')

async def register_handler_chat(dispatcher: Dispatcher):
    register_chat_viber(dispatcher)


async def main(dispatcher: Dispatcher):
    await register_handler_chat(dispatcher)


async def shutdown(dispatcher: Dispatcher):
    logger.error(f"Shutdowning...")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RollerSiteCms.settings')
    executor.start_polling(dp, skip_updates=True, loop=loop, on_shutdown=shutdown, on_startup=main)
