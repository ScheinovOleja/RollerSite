# Register your models here.
from cms.admin.useradmin import PageUserAdmin
from cms.models import PageUser, PageUserGroup
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.apps import apps

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


class MyGroupAdmin(BaseGroupAdmin):
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs['queryset'] = qs.select_related('content_type')
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)


# apps.get_model('login.CustomGroup')._meta.app_label = 'login'
# admin.site.unregister(PageUser)
# admin.site.unregister(PageUserGroup)
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)
admin.site.register(MyUser, CustomUserAdmin)
