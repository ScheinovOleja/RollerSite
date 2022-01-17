# Register your models here.
from django.contrib import admin
from sorl.thumbnail.admin import AdminInlineImageMixin

from rollercms.models import Photo, Gallery, Post, CategoriesPost


class PhotoInline(AdminInlineImageMixin, admin.TabularInline):
    model = Photo
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


class PostAdmin(admin.ModelAdmin):
    fields = ['title_post', 'category', 'image', 'short_description', 'content']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CategoriesPost)
