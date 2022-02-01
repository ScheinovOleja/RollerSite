from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class MailToTgHook(CMSApp):
    app_name = "company"
    name = 'Отправка письма в тг'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["letter.urls"]
