from datetime import datetime

import django
from cms.models import CMSPlugin, Page
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from django.db.models import ImageField, FileField
from djangocms_text_ckeditor.cms_plugins import TextPlugin
from ckeditor.fields import RichTextField


class Gallery(models.Model):
    name = models.CharField('Имя слайдера', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Photo(models.Model):
    title = models.CharField('Заголовок на слайде', max_length=64, null=True, blank=True)
    description = models.TextField('Текст на слайде', max_length=64, null=True, blank=True)
    file = ImageField('Изображение слайда', upload_to='images')
    link = models.ForeignKey(Page, on_delete=models.DO_NOTHING, null=True, blank=True,
                             limit_choices_to={'publisher_is_draft': True}, verbose_name="Ссылка на страницу")
    gallery = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING, verbose_name='Слайдер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайды'


class Slider(CMSPlugin):
    gallery = models.ForeignKey(Gallery, verbose_name='Слайдер', null=True, blank=True, on_delete=models.DO_NOTHING)

    def get_title(self):
        return self.gallery.name

    def __str__(self):
        return self.get_title()


class Tagline(CMSPlugin):
    link = models.ForeignKey(Page, on_delete=models.DO_NOTHING, limit_choices_to={'publisher_is_draft': True},
                             verbose_name="Ссылка на страницу")
    summary_text = models.TextField("Обобщающий текст", max_length=256, null=False, blank=False)
    tagline_title = models.CharField("Слоган верх", max_length=64, null=False, blank=False)
    tagline_subtitle = models.CharField("Слоган низ", max_length=64, null=False, blank=False)
    benefit_1_title = models.CharField("Заголовок преимущества 1", max_length=64, null=False, blank=False)
    benefit_1 = models.TextField("Преимущество 1", max_length=128, null=False, blank=False)
    benefit_2_title = models.CharField("Заголовок преимущества 2", max_length=64, null=False, blank=False)
    benefit_2 = models.TextField("Преимущество 2", max_length=128, null=False, blank=False)


class CreditAndPartnership(CMSPlugin):
    image_1 = FileField('Изображение 1(svg!!!)', upload_to='images')
    title_1 = models.CharField('Заголовок 1', max_length=16, null=False, blank=False)
    description_1 = models.CharField('Описание 1', max_length=32, null=False, blank=False)
    image_2 = FileField('Изображение 2(svg!!!)', upload_to='images')
    title_2 = models.CharField('Заголовок 2', max_length=16, null=False, blank=False)
    description_2 = models.CharField('Описание 2', max_length=32, null=False, blank=False)
    image_3 = FileField('Изображение 3(svg!!!)', upload_to='images')
    title_3 = models.CharField('Заголовок 3', max_length=16, null=False, blank=False)
    description_3 = models.CharField('Описание 3', max_length=32, null=False, blank=False)


class BackCall(CMSPlugin):
    internal_link_wa = models.CharField('Внутренняя ссылка whatsapp', max_length=64, null=False, blank=False)
    external_link_wa = models.CharField('Отображаемая ссылка whatsapp', max_length=64, null=False, blank=False)
    internal_link_vi = models.CharField('Внутренняя ссылка viber', max_length=64, null=False, blank=False)
    external_link_vi = models.CharField('Отображаемая ссылка viber', max_length=64, null=False, blank=False)
    internal_link_tg = models.CharField('Внутренняя ссылка telegram', max_length=64, null=False, blank=False)
    external_link_tg = models.CharField('Отображаемая ссылка telegram', max_length=64, null=False, blank=False)
    text = models.TextField("Текст, который показывается после отправки", max_length=256, null=False, blank=False)


class MyGoogleMap(CMSPlugin):
    city = models.CharField('Город', max_length=64, null=False, blank=False)
    address = models.CharField('Адрес офиса', max_length=64, null=False, blank=False)
    phone = models.CharField('Номер телефона', max_length=64, null=False, blank=False)
    email = models.EmailField('Email', max_length=64, null=False, blank=False)
    map_src = models.URLField('Код карты', max_length=256, null=False, blank=False)


class MyLetterCompany(CMSPlugin):
    big_main_text = models.CharField('Большой основной текст', max_length=256, null=False, blank=False)
    main_text = models.CharField('Основной текст', max_length=256, null=False, blank=False)
    minor_text = models.CharField('Неосновной текст', max_length=256, null=False, blank=False)


class CategoriesPost(models.Model):
    category = models.CharField('Категория поста', max_length=64, null=False, blank=False)


class Post(models.Model):
    title_post = models.CharField('Заголовок поста', max_length=64, null=False, blank=False)
    category = models.ForeignKey(CategoriesPost, verbose_name='Категория поста', null=False, blank=False,
                                 on_delete=models.DO_NOTHING)
    image = FileField('Изображение на странице блога', upload_to='images')
    date_create = models.DateField(auto_created=True, default=django.utils.timezone.now)
    short_description = models.CharField('Краткий текст на странице блога', max_length=128, null=False, blank=False,
                                         default='')
    content = RichTextField(blank=True, null=True)


# class CompanyData(models.Model):
