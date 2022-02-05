from django.contrib import admin

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'order', 'review', 'is_confirm']
    readonly_fields = ['user', 'order', 'review']
    list_filter = ['is_confirm']
