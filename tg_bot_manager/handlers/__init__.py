from aiogram import Dispatcher

from tg_bot_manager.handlers.treatment_back_call import back_call


def register_back_call(dp: Dispatcher):
    dp.register_callback_query_handler(back_call, lambda query: "back_call" in query.data)
