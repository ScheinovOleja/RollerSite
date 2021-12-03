# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ['phone', 'first_name', 'email']
    ordering = ['phone', ]
    fieldsets = (
        (None, {'fields': ('phone', 'password', 'avatar_image')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic', 'email', 'address')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'last_name', 'patronymic', 'email', 'address'),
        }),
    )
    search_fields = ('phone', 'first_name', 'last_name', 'email')
    readonly_fields = ('avatar_image',)

    def delete_queryset(self, request, queryset):
        for user in queryset:
            user.delete()

    def avatar_image(self, obj):
        return mark_safe(obj.avatar)

    avatar_image.short_description = 'Аватар'
    avatar_image.allow_tags = True


admin.site.register(MyUser, CustomUserAdmin)
