import asyncio

from aiogram import Bot, types
from django.shortcuts import render

# Create your views here.
from company.models import AllConstruct


def get_send(request):
    if request.method == 'GET':
        return render(request, 'letter.html')


def send_tg_mail(request):
    loop = asyncio.new_event_loop()
    bot_token = '5182579493:AAH7Yor8nNC2rjL1pb-XafoKfxJxitPyni8'
    bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
    markup = types.InlineKeyboardMarkup()
    message = f"Письмо с сайта:\n" \
              f"Имя - <code>{request.POST['name']}</code>\n" \
              f"Телефон - <code>{request.POST['phone']}</code>\n" \
              f"Email - <code>{request.POST['email']}</code>\n\n" \
              f"Текст обращения:\n" \
              f"{request.POST['text']}"
    loop.run_until_complete(bot.send_message(715845455, message, reply_markup=markup))
    loop.close()