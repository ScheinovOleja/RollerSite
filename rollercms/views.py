import asyncio
import json

import redis
import requests
from aiogram import Bot, types
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

auth_token = '4e48d76e8267dc61-f62f0ce235afa17c-712869435c47c011'  # тут ваш токен полученный в начале #п.2
url = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token, "Content-Type": "application/json"}


# ДЕКОРАТОР ДЛЯ функций и отправки
def sending(func):
    def wrapped(*args):
        return requests.post(url, json.dumps(func(*args)), headers=headers)

    return wrapped


# Отправка текста
@sending
def send_text(agent, text, track=None):
    m = dict(receiver=agent, min_api_version=8, tracking_data=track, type="text", text=text)
    return m


@csrf_exempt
def viber_bot(request):
    if request.method == "POST":
        viber = json.loads(request.body.decode('utf-8'))
        if viber['event'] == 'webhook':
            print(viber)
            print("Webhook успешно установлен")
            return HttpResponse(status=200)
        if viber['event'] == 'message':
            id = viber['sender']['id']
            is_chat = None
            r = redis.StrictRedis(host='localhost', port=6379, db=5)
            for key in r.scan_iter("fsm:*:*:data"):
                is_chat = json.loads(r.get(key))
            loop = asyncio.new_event_loop()
            bot_token = '1753538352:AAGW-cAk2fAT4n5rzp5tnljZIeWa6mD9udo'
            bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
            markup = types.InlineKeyboardMarkup()
            if is_chat:
                markup.add(types.InlineKeyboardButton('Закончить диалог', callback_data=f'exit_chat_{id}_viber'))
            else:
                markup.add(types.InlineKeyboardButton('Начать диалог', callback_data=f'start_chat_{id}_viber'))
            message = f"Сообщение из Viber от пользователя <code>{viber['sender']['name']}</code>:\n\n" \
                      f"{viber['message']['text']}"
            loop.run_until_complete(bot.send_message(715845455, message, reply_markup=markup))
            loop.close()
    return HttpResponse(status=200)


@csrf_exempt
def wa_bot(request):
    print(request)
    # APIUrl = ' https://api.chat-api.com/instance366784/ '
    # token = 'je67vwfvppibji9w'
    # url = f"{self.APIUrl}{method}?token={self.token}"
    # headers = {'Content-type': 'application/json'}
    # answer = requests.post(url, data=json.dumps(data), headers=headers)
    # return answer.json()
