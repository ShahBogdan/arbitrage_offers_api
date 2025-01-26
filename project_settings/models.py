from django.db import models
from ckeditor.fields import RichTextField


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="Мій сайт")
    contact_email = models.EmailField(default="admin@example.com")
    main_page_h1 = models.CharField(
        max_length=255, verbose_name="H1 головної сторінки", default='main h1')
    main_page_title = models.CharField(
        max_length=255, verbose_name="Title головної сторінки", default='title h1')
    main_page_meta_desc = models.CharField(
        max_length=255, verbose_name="Мета опис головної сторінки", default='meta desc')
    main_page_text = RichTextField(
        verbose_name="Текст головної сторінки", default='main text')
    faq_page_title = models.CharField(
        max_length=255, verbose_name="Title FAQ", default='title faq')
    faq_page_h1 = models.CharField(
        max_length=255, verbose_name="H1 для FAQ", default='faq h1')
    faq_page_meta_desc = models.CharField(
        max_length=255, verbose_name="Мета опис FAQ", default='meta desc faq')
    faq_page_text = RichTextField(verbose_name="Текст FAQ", default='faq text')
    pages_title = models.CharField(
        max_length=255, verbose_name="Title категорії Pages", default='pages title')
    pages_page_h1 = models.CharField(
        max_length=255, verbose_name="H1 для категорії Pages", default='pages h1')
    pages_meta_desc = models.CharField(
        max_length=255, verbose_name="Мета опис категорії Pages", default='pages meta desc')
    pages_text = RichTextField(
        verbose_name="Текст категорії Pages", default='pages text')
    enable_feature = models.BooleanField(
        default=True, verbose_name="Робочий стан")

    def __str__(self):
        return "Налаштування сайту"

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"
