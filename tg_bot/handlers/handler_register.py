import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from pony.orm import db_session

from tg_bot.models import LoginMyuser, LoginRegisterfrommessangers
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
    with db_session:
        phone = message.contact.phone_number
        if '+7' in phone:
            index = 2
        else:
            phone = '+' + message.contact.phone_number
            index = 1
        user_phone = phone[index:]
        user = LoginMyuser.get(lambda u: user_phone in u.phone)
        user_messanger = LoginRegisterfrommessangers.get(lambda u: user_phone in u.phone)
        if user_messanger:
            text = 'Спасибо за вашу тягу, но вы уже зарегистрированы!)'
            await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
        else:
            LoginRegisterfrommessangers(
                messenger=0,
                id_messenger=str(message.contact.user_id),
                phone=phone,
                user=user
            )
            text = 'Спасибо за регистрацию!\n\nОжидайте, скоро вам придет оповещение о вашем заказе!'
            await message.answer(text, reply_markup=types.ReplyKeyboardRemove())
    await Registration.in_registered.set()
