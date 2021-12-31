from django.contrib import admin

# Register your models here.
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'order', 'review', 'is_confirm']
    readonly_fields = ['user', 'order', 'review',]


admin.site.register(Review, ReviewAdmin)
