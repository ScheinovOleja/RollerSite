# Create your views here.

from dal import autocomplete
from django.db.models import Q

from .models import Materials, TypeConstruction, ControlType, HardwareColor, MountType, ColorMaterial, PriceCategory


class MaterialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Materials.objects.all()

        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q))

        return qs


class TypeConstructAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = TypeConstruction.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ControlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ControlType.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class HardwareColorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = HardwareColor.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class MountTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = MountType.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class ColorMaterialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ColorMaterial.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class PriceCategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        type_construct = self.forwarded['type_construction']
        qs = PriceCategory.objects.all().filter(gridprice__type_construction=type_construct)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
