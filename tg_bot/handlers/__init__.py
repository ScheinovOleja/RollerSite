from aiogram import Dispatcher

from tg_bot.handlers.chat_handler import get_message
from tg_bot.handlers.chats_for_viber import start_chat, stop_chat, chat
from tg_bot.handlers.handler_register import register, get_number
from tg_bot.handlers.treatment_back_call import back_call
from tg_bot.states.state import Chat, Registration


def register_chat_viber(dp: Dispatcher):
    dp.register_callback_query_handler(start_chat, lambda query: "start_chat_" in query.data, state='*')
    dp.register_message_handler(chat, lambda message: not message.from_user.is_bot, state=Chat.in_chat)
    dp.register_callback_query_handler(stop_chat, lambda query: "exit_chat_" in query.data, state=Chat.in_chat)


def register_back_call(dp: Dispatcher):
    dp.register_callback_query_handler(back_call, lambda query: "back_call" in query.data)


def register_registration(dp: Dispatcher):
    dp.register_message_handler(register, commands=['start'], state='*')
    dp.register_message_handler(get_number, content_types=['contact'], state=Registration.start_register)


def register_all_message(dp: Dispatcher):
    dp.register_message_handler(get_message, state=Registration.in_registered)
