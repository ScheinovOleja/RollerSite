from aiogram import types
from aiogram.dispatcher import FSMContext

from tg_bot_private import bot, dp


async def get_message(message: types.Message, state: FSMContext):
    id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    admin_state = dp.current_state(chat=715845455, user=715845455)
    admin_data = await admin_state.get_data()
    admin_state = await admin_state.get_state()
    if admin_state == 'Chat:in_chat' and admin_data['id'] == str(message.from_user.id):
        markup.add(types.InlineKeyboardButton('Закончить диалог', callback_data=f'exit_chat_{id}_tg'))
    else:
        markup.add(types.InlineKeyboardButton('Начать диалог', callback_data=f'start_chat_{id}_tg'))
    text = f"Сообщение из Telegram от пользователя <a href=\"{message.from_user.url}\">" \
           f"{message.from_user.full_name}</a>:\n\n" \
           f"{message.text}"
    await bot.send_message(1907721147, text, reply_markup=markup, parse_mode='HTML')
