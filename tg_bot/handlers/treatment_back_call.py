from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tg_bot import bot


async def back_call(query: CallbackQuery, state: FSMContext):
    name = query.message.html_text.split('<code>')[1].split('</code>')[0]
    number = query.message.html_text.split('<code>', 2)[2].split('</code>')[0]
    await bot.edit_message_text(f"На звонок по номеру - <code>{number}</code>\nИмя - <code>{name}</code>\n"
                                f"Назначен {query.from_user.full_name}", query.message.chat.id,
                                query.message.message_id)
