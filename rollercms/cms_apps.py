from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BackCallHook(CMSApp):
    app_name = "roller_site"
    name = "Back call"
    _urls = ["roller_site.urls"]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["roller_site.urls"]


apphook_pool.register(BackCallHook)
