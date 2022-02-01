from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class BackCallHook(CMSApp):
    app_name = "roller_site"
    name = "Back call"
    _urls = ["rollercms.urls"]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["rollercms.urls"]


@apphook_pool.register
class BlogHook(CMSApp):
    app_name = "roller_site"
    name = 'Список постов'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["rollercms.urls"]
