import json

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def authentication(request):
    if request.method == "POST" and request.is_ajax():
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                status = '0'
            else:
                status = '1'
        else:
            status = '2'
        some_data_to_dump = {'status': status}
        answer = json.dumps(some_data_to_dump)
        return redirect('/blog')