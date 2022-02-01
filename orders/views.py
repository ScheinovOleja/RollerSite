# Create your views here.
import json

from dal import autocomplete
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from login.models import MyUser
from products.models import GridPrice, HardwareColor, Materials, TypeConstruction


class ChangePrice(View):

    @csrf_exempt
    def post(self, request):
        if request.is_ajax():
            try:
                width = float(request.POST['width'])
                height = float(request.POST['height'])
                count = int(request.POST['count'])
                multiply_value = float(request.POST['multiply'])
                type_construct = request.POST['construct']
                mult = HardwareColor.objects.get_or_none(id=multiply_value)
                spec_type = TypeConstruction.objects.get(id=type_construct)
                if spec_type.is_special:
                    form_price = float(request.POST['price'])
                    price = form_price * mult.multiplication * count * width * height
                else:
                    grid_price = GridPrice.objects.get_or_none(width=width, height=height,
                                                               type_construction=type_construct)
                    price = grid_price.price * mult.multiplication * count
            except ValueError as err:
                return HttpResponse(0, status=200)
            return HttpResponse(price, status=200)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ChangePrice, self).dispatch(*args, **kwargs)


def get_materials(request):
    construct = int(request.POST['construct'])
    materials = Materials.objects.filter(type_construction=construct)
    spec_construct = TypeConstruction.objects.get(id=construct)
    all_material = {f'{material.color}/{material.name}/{material.type_construction}': material.id for material in
                    materials}
    all_material['is_special'] = True if spec_construct.is_special else False
    json_material = json.dumps(all_material, ensure_ascii=False).encode('utf-8')
    return HttpResponse(json_material.decode(), status=200)


def get_special_construction(request):
    construct = int(request.POST['construct'])
    spec_construct = TypeConstruction.objects.filter(name=construct)
    if spec_construct.is_special:
        return HttpResponse(True, status=200)
    else:
        return HttpResponse(False, status=200)


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MyUser.objects.all().filter(is_staff=False)

        if self.q:
            qs = qs.filter(Q(first_name__istartswith=self.q) | Q(last_name__istartswith=self.q) |
                           Q(patronymic__istartswith=self.q))

        return qs
