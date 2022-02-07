from django.contrib import admin

# Register your models here.
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.safestring import mark_safe

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    fields = ['user', 'order', 'review', 'is_confirm']
    readonly_fields = ['user', 'order', 'review']
    list_display = ['order', 'is_confirm', 'accept_display', 'reject_display']
    list_filter = ['is_confirm']

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [path(r'accept/<pk>', self.admin_site.admin_view(self.accept), name="accept"),
                      path(r'reject/<pk>', self.admin_site.admin_view(self.reject), name="reject")
                      ]
        return shard_urls + urls

    def accept_display(self, obj):
        if obj.is_confirm == 0:
            url = f'<a href="{reverse(f"admin:accept", args=(obj.id,))}">Принять отзыв</a>'
        elif obj.is_confirm == 1:
            url = f'<span>Отзыв одобрен</span>'
        else:
            url = f'<a href="{reverse(f"admin:accept", args=(obj.id,))}">Принять отзыв</a>'
        return mark_safe(url)

    def reject_display(self, obj):
        if obj.is_confirm == 0:
            url = f'<a href="{reverse(f"admin:reject", args=(obj.id,))}">Отклонить отзыв</a>'
        elif obj.is_confirm == 1:
            url = f'<a href="{reverse(f"admin:reject", args=(obj.id,))}">Отклонить отзыв</a>'
        else:
            url = f'<span>Отзыв отклонен</span>'
        return mark_safe(url)

    def accept(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.is_confirm = 1
        review.save()
        return HttpResponseRedirect(reverse(f'admin:reviews_review_changelist'))

    def reject(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.is_confirm = 2
        review.save()
        return HttpResponseRedirect(reverse(f'admin:reviews_review_changelist'))

    accept_display.short_description = 'Одобрить'
    reject_display.short_description = 'Отклонить'
