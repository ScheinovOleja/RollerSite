import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tg_bot import connection
from tg_bot.states.state import Registration


async def register(message: Message, state: FSMContext):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    )
    text = 'Для того, чтобы зарегистрироваться, вам необходимо предоставить ваш номер телефона, путем нажатия на ' \
           'кнопку ниже!'
    await Registration.start_register.set()
    await message.answer(text, reply_markup=markup)


def re_fn(expr, item):
    reg = re.compile(expr, re.I)
    return reg.search(item) is not None


async def get_number(message: types.Message, state: FSMContext):
    regex = r'^(8|\+7)' + '(' + message.contact.phone_number[2:] + ')'
    connection.create_function("REGEXP", 2, re_fn)
    cursor = connection.cursor()
    test = 'SELECT * FROM login_myuser ' \
           'WHERE login_myuser.phone REGEXP "{regex}"'.format(regex=regex)
    cursor.execute(test)
    user_from_site = cursor.fetchone()
    cursor.execute(f'''
        SELECT * FROM login_registerfrommessangers
        WHERE login_registerfrommessangers.messenger == 0 and
              login_registerfrommessangers.id_messenger == {message.contact.user_id} and
              login_registerfrommessangers.phone == {message.contact.phone_number}
    ''')
    user = cursor.fetchone()
    if user:
        text = 'Спасибо за вашу тягу, но вы уже зарегистрированы!)'
        await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    else:
        cursor.execute(f'''
                    INSERT INTO login_registerfrommessangers (messenger, id_messenger, phone, user_id)
                    VALUES (0, {message.contact.user_id}, {message.contact.phone_number}, {user_from_site[0]});
                    ''')
        connection.commit()
        text = 'Спасибо за регистрацию!\n\nОжидайте, скоро вам придет оповещение о вашем заказе!'
        await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await Registration.in_registered.set()
