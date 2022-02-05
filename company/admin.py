from cms.admin.pageadmin import PageTypeAdmin, PageAdmin
from cms.admin.settingsadmin import SettingsAdmin
from cms.admin.static_placeholder import StaticPlaceholderAdmin
from cms.models import Page, PageType, StaticPlaceholder, UserSettings
from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from company.forms import TemplatesModelForm
from company.models import AllConstruct, Construct
from login.admin import CustomUserAdmin
from login.models import MyUser
from orders.admin import OrderAdmin
from orders.models import Order
from products.admin import GridPriceAdmin, MaterialsAdmin, ColorMaterialAdmin, HardwareColorAdmin, MountTypeAdmin, \
    ControlTypeAdmin, TypeConstructionAdmin, ProductListAdmin
from products.models import ProductList, GridPrice, Materials, TypeConstruction, ControlType, MountType, \
    PriceCategory, HardwareColor, ColorMaterial
from reviews.admin import ReviewAdmin
from reviews.models import Review
from rollercms.admin import GalleryAdmin, PostAdmin
from rollercms.models import Gallery, Post, CategoriesPost


class AllConstructAdmin(admin.ModelAdmin):
    form = TemplatesModelForm


class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)
        # Sort the apps alphabetically.
        app_list = list(app_dict.values())
        # app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        # for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list


admin.site = MyAdminSite()

admin.site.register(Order, OrderAdmin)
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ProductList, ProductListAdmin)
admin.site.register(TypeConstruction, TypeConstructionAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(ColorMaterial, ColorMaterialAdmin)
admin.site.register(PriceCategory)
admin.site.register(GridPrice, GridPriceAdmin)
admin.site.register(HardwareColor, HardwareColorAdmin)
admin.site.register(ControlType, ControlTypeAdmin)
admin.site.register(MountType, MountTypeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(CategoriesPost)
admin.site.register(Post, PostAdmin)
admin.site.register(AllConstruct, AllConstructAdmin)
admin.site.register(Construct)

admin.site.register(UserSettings, SettingsAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(PageType, PageTypeAdmin)
admin.site.register(StaticPlaceholder, StaticPlaceholderAdmin)
