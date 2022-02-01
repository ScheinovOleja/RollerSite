from django.contrib import admin

# Register your models here.
from products.forms import PersonForm
from products.models import ProductList, GridPrice, Materials, TypeConstruction, ControlType, MountType, \
    TypeFabricMeasurement, PriceCategory, HardwareColor


class GridPriceAdmin(admin.ModelAdmin):
    form = PersonForm


class MaterialsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


class TypeConstructionAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ControlTypeAdmin(admin.ModelAdmin):
    search_fields = ['type_control']


class MountTypeAdmin(admin.ModelAdmin):
    search_fields = ['mount_type']


class TypeFabricMeasurementAdmin(admin.ModelAdmin):
    search_fields = ['type_measurement']


class HardwareColorAdmin(admin.ModelAdmin):
    search_fields = ['color']


admin.site.register(ProductList)
admin.site.register(GridPrice, GridPriceAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(TypeConstruction, TypeConstructionAdmin)
admin.site.register(ControlType, ControlTypeAdmin)
admin.site.register(MountType, MountTypeAdmin)
admin.site.register(TypeFabricMeasurement, TypeFabricMeasurementAdmin)
admin.site.register(PriceCategory)
admin.site.register(HardwareColor, HardwareColorAdmin)
