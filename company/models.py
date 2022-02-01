from ckeditor_uploader.fields import RichTextUploadingField
from cms.models import Page, CMSPlugin
from django.db import models


class AboutCompany(models.Model):
    logo = models.TextField('Аватар', max_length=99999)


class AllConstruct(CMSPlugin):
    image_file = models.FileField(upload_to='construct_types/', null=False, blank=False,)
    image = models.CharField('Изображение на карточке', max_length=9999999, default='')
    category = models.CharField('Название конструкции', null=False, blank=False, max_length=64)
    type_construct = models.ForeignKey(Page, on_delete=models.DO_NOTHING, verbose_name='Страница показа конструкции',
                                       limit_choices_to={'publisher_is_draft': False})

    def save(self, no_signals=False, *args, **kwargs):
        if self.image_file.name.endswith('.svg'):
            self.image = self.image_file.read().decode()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category}'


class Construct(models.Model):
    name = models.OneToOneField(AllConstruct, on_delete=models.DO_NOTHING, verbose_name='Название конструкции')
    content = RichTextUploadingField(config_name='default', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'