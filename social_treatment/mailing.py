import asyncio

from aiogram import Bot, types
from django.http import HttpResponse

from rollercms.views import send_register_from_site, viber_send_order_to_user


def send_order(phone, messenger_user=None, text=None, file=None):
    if messenger_user.messenger == 0:
        loop = asyncio.new_event_loop()
        bot_token = '5125599420:AAFvc7hcTAR-nOT26w1zq2-SEPO-M9PCtMY'
        bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
        loop.run_until_complete(bot.send_message(messenger_user.id_messenger, text))
        if file:
            loop.run_until_complete(bot.send_document(messenger_user.id_messenger, (file.name.split("/")[-1], file)))
        loop.close()
    elif messenger_user.messenger == 1:
        viber_send_order_to_user(phone, messenger_user.id_messenger, text, file)
    elif messenger_user.messenger == 2:
        pass


def send_register_user(phone, password=None, messenger_user=None, text=None):
    if messenger_user.messenger == 0:
        message = f"Доброго времени суток!\n\n" \
                  f"Вы зарегистрированы на сайте group-mgr.ru!\n" \
                  f"Ваши данные для входа на сайт:\n" \
                  f"Логин - <code>{phone}</code>,\n" \
                  f"Пароль - <code>{password}</code>.\n\n" \
                  f"Обязательно смените пароль!!"
        loop = asyncio.new_event_loop()
        bot_token = '5125599420:AAFvc7hcTAR-nOT26w1zq2-SEPO-M9PCtMY'
        bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
        loop.run_until_complete(bot.send_message(messenger_user.id_messenger, message))
        loop.close()
    elif messenger_user.messenger == 1:
        send_register_from_site(phone, messenger_user.id_messenger, text)
    elif messenger_user.messenger == 2:
        pass


def mailing(request):
    if request.is_ajax:
        loop = asyncio.new_event_loop()
        bot_token = '5130851592:AAHUYDFIdfACcaB1U3tx39QyVdCvL1GZG3I'
        bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Подтвердить звонок', callback_data='back_call'))
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        message = f"Запрос на обратный звонок!\n" \
                  f"Имя - <code>{name}</code>\n" \
                  f"Номер телефона - <code>{phone}</code>\n"
        loop.run_until_complete(bot.send_message(-759551434, message, reply_markup=markup))
        loop.close()
    return HttpResponse()
