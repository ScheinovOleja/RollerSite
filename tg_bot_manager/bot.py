import os
import sys

sys.path.append('/root/RollerSite/')

from asyncio.log import logger

from aiogram import Dispatcher
from aiogram.utils import executor

from tg_bot_manager import dp, loop
from tg_bot_manager.handlers import register_back_call


async def register_back_call_manager(dispatcher: Dispatcher):
    register_back_call(dispatcher)


async def main(dispatcher: Dispatcher):
    await register_back_call_manager(dispatcher)


async def shutdown(dispatcher: Dispatcher):
    logger.error(f"Shutdowning...")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RollerSiteCms.settings')
    executor.start_polling(dp, skip_updates=True, loop=loop, on_shutdown=shutdown, on_startup=main)
