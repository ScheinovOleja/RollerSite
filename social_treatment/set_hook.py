import json

import requests


def set_hook():
    auth_token = '4e48d76e8267dc61-f62f0ce235afa17c-712869435c47c011'  # тут ваш токен полученный в начале #п.2
    hook = 'https://chatapi.viber.com/pa/set_webhook'
    headers = {'X-Viber-Auth-Token': auth_token, "Content-Type": "application/json"}

    sen = dict(url='https://7b46-185-90-100-198.ngrok.io/ru/webhook/vibermsgget/',
               event_types=["conversation_started", "message"],
               send_name=True,
               )

    test = json.dumps(sen)
    r = requests.post(hook, test, headers=headers)
    print(r.json())


if __name__ == '__main__':
    set_hook()
