from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    start_register = State()
    in_registered = State()
