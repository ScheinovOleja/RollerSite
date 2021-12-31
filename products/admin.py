from django.contrib import admin

# Register your models here.
from products.models import ProductList, GridPrice, Materials, TypeConstruction, ControlType, MountType, \
    TypeFabricMeasurement, PriceCategory, HardwareColor

admin.site.register(ProductList)
admin.site.register(GridPrice)
admin.site.register(Materials)
admin.site.register(TypeConstruction)
admin.site.register(ControlType)
admin.site.register(MountType)
admin.site.register(TypeFabricMeasurement)
admin.site.register(PriceCategory)
admin.site.register(HardwareColor)
