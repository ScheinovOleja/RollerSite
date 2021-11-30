from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import Slider, Tagline, CreditAndPartnership, BackCall, MyGoogleMap


class SliderPlugin(CMSPluginBase):
    module = _("Самодельные плагины")
    name = _("Слайдер")
    render_template = "blocks/slider.html"
    model = Slider

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class TaglinePlugin(CMSPluginBase):
    module = _("Самодельные плагины")
    name = _("Слоган и преимущества")
    render_template = "blocks/tagline.html"
    model = Tagline

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class CreditPlugin(CMSPluginBase):
    module = _("Самодельные плагины")
    name = _("Информация о кредите")
    render_template = "blocks/credit.html"
    model = CreditAndPartnership

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class PartnershipPlugin(CMSPluginBase):
    module = _("Самодельные плагины")
    name = _("Информация о партнерах")
    render_template = "blocks/partnership.html"
    model = CreditAndPartnership

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class BackCallPlugin(CMSPluginBase):
    module = _('Самодельные плагины')
    name = _('Обратный звонок')
    render_template = "blocks/back_call.html"
    model = BackCall

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class MyGoogleMapPlugin(CMSPluginBase):
    module = _('Самодельные плагины')
    name = _('Карта')
    render_template = "blocks/google_map.html"
    model = MyGoogleMap

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(SliderPlugin)
plugin_pool.register_plugin(TaglinePlugin)
plugin_pool.register_plugin(CreditPlugin)
plugin_pool.register_plugin(PartnershipPlugin)
plugin_pool.register_plugin(BackCallPlugin)
plugin_pool.register_plugin(MyGoogleMapPlugin)
