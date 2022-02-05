from aiogram import Dispatcher

from tg_bot_private.handlers.chats_for_viber import start_chat, chat, stop_chat, register
from tg_bot_private.states.state import Chat


def register_chat_viber(dp: Dispatcher):
    dp.register_message_handler(register, commands=['/start'], state='*')
    dp.register_callback_query_handler(start_chat, lambda query: "start_chat_" in query.data, state=Chat.non_chat)
    dp.register_message_handler(chat, lambda message: not message.from_user.is_bot, state=Chat.in_chat)
    dp.register_callback_query_handler(stop_chat, lambda query: "exit_chat_" in query.data, state=Chat.in_chat)
