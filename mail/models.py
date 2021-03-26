from django.db import models

# Create your models here.

class Mail(models.Model):

    surname = models.CharField('Фамилия',max_length=255)
    lastname = models.CharField('Отчество',max_length=255)
    name = models.CharField('Имя',max_length=255)
    email = models.EmailField('Почта')
    phone = models.CharField('Контактный телефон:',max_length=255)
    universityjob = models.CharField('Вуз',max_length=255,blank=True,null=True)
    position = models.CharField('Должность',max_length=255,blank=True,null=True)
    consent = models.BooleanField('Согласие',blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
