from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import re_path

from company.views import ConstructDetailView, test


@apphook_pool.register
class AllConstructHook(CMSApp):
    app_name = "company"
    name = 'Все виды конструкций'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["company.urls"]
