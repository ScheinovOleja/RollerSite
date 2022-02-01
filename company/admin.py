from django.contrib import admin

# Register your models here.
from company.forms import TemplatesModelForm
from company.models import AllConstruct, Construct

admin.site.register(Construct)


@admin.register(AllConstruct)
class TemplatesAdmin(admin.ModelAdmin):
    form = TemplatesModelForm
