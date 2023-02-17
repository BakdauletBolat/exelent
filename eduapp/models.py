from django.db import models
from django.urls import reverse


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание')
    subTitle = models.CharField(max_length=255, blank=True, null=True, verbose_name='Под описание')
    image = models.ImageField(upload_to='SlideImages/', verbose_name='Картинка')
    linkTo = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каруселька'
        verbose_name_plural = 'Каруселька'


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    shortDescription = models.TextField(verbose_name='Краткое описание')
    image = models.ImageField(upload_to="PageImages/", verbose_name='Картинка')
    file = models.FileField(upload_to='PdfFile/', null=True, blank=True, verbose_name='Файл')
    description = models.TextField(verbose_name='Полное описание')

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
