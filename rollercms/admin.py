# Register your models here.
from django.contrib import admin
from sorl.thumbnail.admin import AdminInlineImageMixin

from rollercms.models import Photo


class PhotoInline(AdminInlineImageMixin, admin.TabularInline):
    model = Photo
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
