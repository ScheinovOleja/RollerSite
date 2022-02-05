from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.utils.markdown import hlink, link, code, hcode

from tg_bot_private import bot, dp


async def get_message(message: types.Message, state: FSMContext):
    id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    admin_state = dp.current_state(chat=1907721147, user=1907721147)
    admin_data = await admin_state.get_data()
    admin_state = await admin_state.get_state()
    code_text = link(message.from_user.full_name, message.from_user.url)
    if admin_state == 'Chat:in_chat' and admin_data['id'] == str(message.from_user.id):
        markup.add(types.InlineKeyboardButton('Закончить диалог', callback_data=f'exit_chat_{id}_tg'))
    else:

        markup.add(types.InlineKeyboardButton('Начать диалог', callback_data=f'start_chat_{id}_tg'))
    try:
        text = f"Сообщение из Telegram от пользователя {code_text}:\n\n" \
               f"{message.text}"
    except Exception as err:
        text = f"Сообщение из Telegram от пользователя {code_text}:\n\n" \
               f"{message.text}"
    await bot.send_message(1907721147, text, reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
