from dal import autocomplete
from django import forms

from products.models import Materials, ProductList


class PersonForm(forms.ModelForm):

    class Meta:
        model = Materials
        fields = '__all__'
        widgets = {
            'material': autocomplete.ModelSelect2(url='material-autocomplete', forward=['type_construction'])
        }


class ProductListAutocompleteForm(forms.ModelForm):

    class Meta:
        model = ProductList
        fields = '__all__'
        widgets = {
            'type_construction': autocomplete.ModelSelect2(url='type_construct-autocomplete'),
            'material': autocomplete.ModelSelect2(url='material-autocomplete', forward=['type_construction']),
            'control_type': autocomplete.ModelSelect2(url='control_type-autocomplete'),
            'hardware_color': autocomplete.ModelSelect2(url='hardware_color-autocomplete'),
            'mount_type': autocomplete.ModelSelect2(url='mount_type-autocomplete'),
            'type_of_fabric_measurement': autocomplete.ModelSelect2(url='type_fabric-autocomplete'),
        }
