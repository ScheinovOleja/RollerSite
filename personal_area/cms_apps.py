from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ChangePassOrEmail(CMSApp):
    app_name = 'personal_area'
    name = 'Смена пароля и почты'
    _urls = ["personal_area.urls"]

    def get_urls(self, page=None, language=None, **kwargs):
        return ["personal_area.urls"]
