from django.db import models

class TypeSeminar(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='TypeSeminar/',null=True,blank=True)

    class Meta:

        verbose_name = "Тип семинара"
        verbose_name_plural = "Типы семинара"

    def __str__(self):
        return self.name

class Mail(models.Model):

    surname = models.CharField('Фамилия',max_length=255)
    lastname = models.CharField('Отчество',max_length=255)
    name = models.CharField('Имя',max_length=255)
    email = models.EmailField('Почта')
    phone = models.CharField('Контактный телефон:',max_length=255)
    universityjob = models.CharField('Вуз',max_length=255,blank=True,null=True)
    position = models.CharField('Должность',max_length=255,blank=True,null=True)
    typeSeminar = models.ForeignKey(TypeSeminar,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Тип семинара')
    consent = models.BooleanField('Согласие',blank=True,null=True)
    created_at = models.DateTimeField('Дата',auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
