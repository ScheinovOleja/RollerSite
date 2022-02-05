from dal import autocomplete
from django import forms

from products.models import Materials, ProductList


class PersonForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'
        widgets = {
            'material': autocomplete.ModelSelect2(url='material-autocomplete')
        }


class ProductListAutocompleteForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = '__all__'
        widgets = {
            'type_construction': autocomplete.ModelSelect2(url='type_construct-autocomplete'),
            'material': autocomplete.ModelSelect2(url='material-autocomplete'),
            'color_material': autocomplete.ModelSelect2(url='color_material-autocomplete'),
            'price_category': autocomplete.ModelSelect2(url='price_category-autocomplete',
                                                        forward=['type_construction']),
            'control_type': autocomplete.ModelSelect2(url='control_type-autocomplete'),
            'hardware_color': autocomplete.ModelSelect2(url='hardware_color-autocomplete'),
            'mount_type': autocomplete.ModelSelect2(url='mount_type-autocomplete'),
        }
