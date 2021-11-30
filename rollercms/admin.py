# Register your models here.
from django.contrib import admin
from sorl.thumbnail.admin import AdminInlineImageMixin

from rollercms.models import Photo, Gallery


# from .forms import CustomUserCreationForm, CustomUserChangeForm


class PhotoInline(AdminInlineImageMixin, admin.TabularInline):
    model = Photo
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', ]


admin.site.register(Gallery, GalleryAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)
