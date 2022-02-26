from ckeditor_uploader.fields import RichTextUploadingField
from cms.models import Page, CMSPlugin
from django.db import models


class AllConstruct(CMSPlugin):
    class Meta:
        verbose_name = 'Тип конструкции на сайте'
        verbose_name_plural = 'Все типы конструкций на сайте'

    image_file = models.FileField(upload_to='construct_types/', null=False, blank=False,)
    image = models.CharField('Изображение на карточке', max_length=9999999, default='')
    category = models.CharField('Название конструкции', null=False, blank=False, max_length=64)
    type_construct = models.ForeignKey(Page, on_delete=models.DO_NOTHING, verbose_name='Страница показа конструкции',
                                       limit_choices_to={'publisher_is_draft': False})

    def __str__(self):
        return f'{self.category}'


class Construct(models.Model):
    class Meta:
        verbose_name = 'Описание конструкции'
        verbose_name_plural = 'Все описания конструкций на сайте'

    name = models.OneToOneField(AllConstruct, on_delete=models.DO_NOTHING, verbose_name='Название конструкции')
    content = RichTextUploadingField(config_name='default', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
