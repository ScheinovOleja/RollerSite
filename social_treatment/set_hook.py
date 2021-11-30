import json

import requests

auth_token = '4e48d76e8267dc61-f62f0ce235afa17c-712869435c47c011'  # тут ваш токен полученный в начале #п.2
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token, "Content-Type": "application/json"}

sen = dict(url='https://65da-185-90-100-198.ngrok.io/ru/webhook/vibermsgget/',
           event_types=["message"],
           send_name=True,
           send_photo=True
           )
# sen - это body запроса для отправки к backend серверов viber
# seen, delivered - можно убрать, но иногда маркетологи хотят знать,
# сколько и кто именно  принял и почитал ваших сообщений,  можете оставить)

r = requests.post(hook, json.dumps(sen), headers=headers)
# r - это пост запрос составленный по требованиям viber
print(r.json())
# в ответном print мы должны увидеть "status_message":"ok" - и это значит,
#  что вебхук установлен
