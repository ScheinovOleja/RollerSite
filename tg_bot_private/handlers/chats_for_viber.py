from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from viberbot import BotConfiguration, Api
from viberbot.api.messages import TextMessage

from tg_bot import bot
from tg_bot_private.states.state import Chat


async def start_chat(query: CallbackQuery, state: FSMContext):
    if '_viber' in query.data:
        await state.update_data({'chat': 'viber'})
    elif '_tg' in query.data:
        await state.update_data({'chat': 'tg'})
    else:
        await state.update_data({'chat': 'whatsapp'})
    await state.update_data({'id': query.data.split('_')[2]})
    text = f'Начат чат с пользователем <code>{query.message.md_text.split("[", 1)[1].split("]")[0]}</code>.'
    await query.message.answer(text)
    await Chat.in_chat.set()


async def chat(message: Message, state: FSMContext):
    data = await state.get_data()
    if 'tg' == data['chat']:
        return await chat_tg(message, state)
    elif 'viber' == data['chat']:
        return await chat_viber(message, state)


async def chat_tg(message: Message, state: FSMContext):
    data = await state.get_data()
    id = data['id']
    await bot.send_message(id, text=message.text)


async def chat_viber(message: Message, state: FSMContext):
    bot_configuration = BotConfiguration(
        name='TestBot',
        auth_token='4e48d76e8267dc61-f62f0ce235afa17c-712869435c47c011',
        avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/5068/3a16f76a7e761ec45269a18f097bf2e02a3f28c'
               'f2d21099505de3c14db3a5068.jpg'
    )
    viber = Api(bot_configuration)
    data = await state.get_data()
    id = data['id']
    message = TextMessage(
        text=message.text
    )
    viber.send_messages(id, message)


async def stop_chat(query: CallbackQuery, state: FSMContext):
    text = f'Закончен чат с пользователем <code>{query.message.md_text.split("`", 1)[1].split("`")[0]}</code>.'
    await Chat.non_chat.set()
    await query.message.answer(text)


async def register(message: Message, state: FSMContext):
    if message.from_user.id == 1907721147 or message.from_user.id == 715845455:
        await Chat.non_chat.set()
        await message.answer('Поздравляю, теперь ты могёшь общаться со своими покупателями!)')
