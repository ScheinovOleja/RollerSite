"""RollerSiteCms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

from login.authentication import authentication
from orders.views import UserAutocomplete
from products.views import MaterialAutocomplete, ControlTypeAutocomplete, TypeConstructAutocomplete, \
    HardwareColorAutocomplete, MountTypeAutocomplete, TypeFabricMeasurementAutocomplete
from social_treatment.mailing import mailing

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    re_path("admin/", admin.site.urls),
    re_path('^material-autocomplete/', MaterialAutocomplete.as_view(), name='material-autocomplete'),
    re_path('^type_construct-autocomplete/', TypeConstructAutocomplete.as_view(), name='type_construct-autocomplete'),
    re_path('^control_type-autocomplete/', ControlTypeAutocomplete.as_view(), name='control_type-autocomplete'),
    re_path('^hardware_color-autocomplete/', HardwareColorAutocomplete.as_view(), name='hardware_color-autocomplete'),
    re_path('^mount_type-autocomplete/', MountTypeAutocomplete.as_view(), name='mount_type-autocomplete'),
    re_path('^type_fabric-autocomplete/', TypeFabricMeasurementAutocomplete.as_view(),
            name='type_fabric-autocomplete'),
    re_path('^user-autocomplete/', UserAutocomplete.as_view(), name='user-autocomplete'),
    re_path('mailing/', mailing),
    re_path('login_user/', authentication),
    re_path('webhook/', include('rollercms.urls')),
    re_path('^accounts/', include('login.urls')),
    re_path('^ajax_calc/', include('orders.urls')),
    re_path("", include("cms.urls")),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
