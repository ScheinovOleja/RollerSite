from django.forms import ModelForm

from company.models import AllConstruct


class TemplatesModelForm(ModelForm):

    class Meta:
        model = AllConstruct
        fields = ('image_file', 'category', 'type_construct')

