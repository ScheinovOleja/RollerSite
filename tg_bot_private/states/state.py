from aiogram.dispatcher.filters.state import StatesGroup, State


class Chat(StatesGroup):
    non_chat = State()
    in_chat = State()
