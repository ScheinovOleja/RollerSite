from django.contrib import admin

# Register your models here.


class GridPriceAdmin(admin.ModelAdmin):
    ordering = ['type_construction']


class MaterialsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


class ColorMaterialAdmin(admin.ModelAdmin):
    search_fields = ['color']
    ordering = ['color']


class TypeConstructionAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ControlTypeAdmin(admin.ModelAdmin):
    search_fields = ['type_control']


class MountTypeAdmin(admin.ModelAdmin):
    search_fields = ['mount_type']


class HardwareColorAdmin(admin.ModelAdmin):
    search_fields = ['color']


class ProductListAdmin(admin.ModelAdmin):
    search_fields = ['order']
    date_hierarchy = 'order__create_date'
