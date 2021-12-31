import asyncio
import json
import redis2
from aiogram import Bot, types
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, ContactMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberMessageRequest

from login.models import RegisterFromMessangers, MyUser
from orders.models import Order
from reviews.models import Review

bot_configuration = BotConfiguration(
    name='TestBot',
    auth_token='4e48d76e8267dc61-f62f0ce235afa17c-712869435c47c011',
    avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/5068/3a16f76a7e761ec45269a18f097bf2e02a3f28c'
           'f2d21099505de3c14db3a5068.jpg'
)
viber = Api(bot_configuration)


def send_register_from_site(phone, viber_id, text):
    message = TextMessage(text=text)
    viber.send_messages(viber_id, message)


def conversation(viber_request):
    id = viber_request.user.id
    if not viber_request.subscribed:
        message = TextMessage(
            text='Данный бот предназначен для общения и регистрации.\n\n'
                 'Чтобы зарегистрироваться в боте, введите команду *```start```*'
        )
        viber.send_messages(id, message)


def chat_viber_tg(viber):
    id = viber.sender.id
    is_chat = None
    r = redis2.StrictRedis(host='localhost', port=6379, db=2)
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
    message = f"Сообщение из Viber от пользователя <code>{viber.sender.name}</code>:\n\n" \
              f"{viber.message.text}"
    loop.run_until_complete(bot.send_message(715845455, message, reply_markup=markup))
    loop.close()


@csrf_exempt
def wa_bot(request):
    print(request)


def message_treatment(viber_request):
    if isinstance(viber_request.message, ContactMessage):
        regex = r'^(8|\+7)' + '(' + viber_request.message.contact.phone_number[1:] + ')'
        user_from_site = MyUser.objects.get_or_none(phone__regex=regex)
        user = RegisterFromMessangers.objects.get_or_create(
            messenger=1,
            id_messenger=viber_request.sender.id,
            phone=viber_request.message.contact.phone_number,
            defaults={
                'user': user_from_site
            }
        )
        if not user[1]:
            message = TextMessage(text='Спасибо за вашу тягу, но вы уже зарегистрированы!)')
            viber.send_messages(viber_request.sender.id, message)
        else:
            message = TextMessage(text='Спасибо за регистрацию!\n\n'
                                       'Ожидайте, скоро вам придет оповещение о вашем заказе!')
            viber.send_messages(viber_request.sender.id, message)
    if isinstance(viber_request.message, TextMessage):
        if viber_request.message.text.lower() == 'start':
            id = viber_request.sender.id
            keyboard = {
                "InputFieldState": 'hidden',
                "DefaultHeight": False,
                "Buttons": [
                    {
                        "BgColor": "#808080",
                        "ActionType": "share-phone",
                        "ActionBody": 'Номер телефона',
                        "Text": "Мой номер",
                    }
                ]
            }
            message = TextMessage(keyboard=keyboard, text='Чтобы продолжить, отправьте ваш номер телефона, '
                                                          'нажатием на кнопку ниже!', min_api_version=7)
            viber.send_messages(id, message)
        elif '/review' in viber_request.message.text.lower():
            id = viber_request.sender.id
            text = viber_request.message.text.split('/review ')[1]
            num_order = text.split('\n')[0]
            text_review = text.split('\n')[1]
            order = Order.objects.get_or_none(num_order=num_order)
            if not order:
                message = TextMessage(text='Вы ввели неверный номер заказа!\n\n'
                                           'Проверьте правильность написания номера заказа!', min_api_version=7)
                viber.send_messages(id, message)
            else:
                review = Review.objects.get_or_create(
                    review=text_review,
                    user=order.user,
                    defaults={
                        'order': order
                    }
                )
                if not review[1]:
                    message = TextMessage(
                        text='Вы уже оставляли отзыв на данный заказ!', min_api_version=7)
                    viber.send_messages(id, message)
                else:
                    message = TextMessage(
                        text='Спасибо за отзыв!\n\nПосле проверки на цензуру ваш отзыв будет опубликован '
                             'на нашем сайте!', min_api_version=7)
                    viber.send_messages(id, message)
        else:
            chat_viber_tg(viber_request)


@csrf_exempt
def post(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body.decode('utf-8'))
        if viber_request.event_type == 'webhook':
            print(viber_request)
            print("Webhook успешно установлен")
            return HttpResponse(status=200)
        if isinstance(viber_request, ViberConversationStartedRequest):
            conversation(viber_request)
        if isinstance(viber_request, ViberMessageRequest):
            message_treatment(viber_request)
    return HttpResponse(status=200)
