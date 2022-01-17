from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import path


@apphook_pool.register
class ReviewHook(CMSApp):
    app_name = "roller_site"
    name = 'Отзывы о компании'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["reviews.urls"]
