import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from tg_bot import bot
from tg_bot.states.state import Chat


async def get_message(message: types.Message, state: FSMContext):
    id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    data = await state.get_data()
    if await state.get_state() == Chat.in_chat:
        markup.add(types.InlineKeyboardButton('Закончить диалог', callback_data=f'exit_chat_{id}_tg'))
    else:
        markup.add(types.InlineKeyboardButton('Начать диалог', callback_data=f'start_chat_{id}_tg'))
    text = f"Сообщение из Telegram от пользователя <code>{message.from_user.full_name}</code>:\n\n" \
           f"{message.text}"
    await bot.send_message(715845455, text, reply_markup=markup)
