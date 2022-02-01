from dal import autocomplete
from django import forms

from orders.models import Order


class UserAutocompleteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'user': autocomplete.ModelSelect2(url='user-autocomplete')
        }
