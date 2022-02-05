from aiogram import Dispatcher

from tg_bot.handlers.chat_handler import get_message
from tg_bot.handlers.handler_register import register, get_number
from tg_bot.handlers.review_handler import reviews_reg
from tg_bot.states.state import Registration


def register_reviews(dp: Dispatcher):
    dp.register_message_handler(reviews_reg, commands=['review'], state='*')


def register_registration(dp: Dispatcher):
    dp.register_message_handler(register, commands=['start'], state='*')
    dp.register_message_handler(get_number, content_types=['contact'], state=Registration.start_register)


def register_all_message(dp: Dispatcher):
    dp.register_message_handler(get_message, state=Registration.in_registered)
