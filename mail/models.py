from django.db import models

# Create your models here.

class Mail(models.Model):

    name = models.CharField('name',max_length=255)
    email = models.EmailField('email')
    content = models.TextField('content')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Сообщения"
        verbose_name_plural = "Сообщений"
