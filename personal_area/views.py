from django.shortcuts import render

# Create your views here.
from django.views import View


class ChangeAvatar(View):

    def get(self, request):
        return render(request, template_name='personal_area.html')

    def post(self, request):
        if request.POST:
            print(request)
