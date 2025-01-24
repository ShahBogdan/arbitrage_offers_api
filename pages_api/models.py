from django.db import models
from ckeditor.fields import RichTextField
from slugify import slugify


class Page (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        unique=True, max_length=255, verbose_name="URL-имя", blank=True, null=True)

    title = models.CharField(
        max_length=255, verbose_name="Назва", default='NEW PAGE')
    meta_title = models.CharField(
        max_length=255, verbose_name="Мета заголовок")
    meta_description = models.CharField(
        max_length=255, verbose_name="Мета опис")
    image = models.ImageField(upload_to='pages/', verbose_name='Зображення')
    h1 = models.CharField(
        max_length=255, verbose_name="Заголовок")
    text = RichTextField()
    show_in_main_menu = models.BooleanField(
        default=False, verbose_name="Показувати в головному меню ?")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
