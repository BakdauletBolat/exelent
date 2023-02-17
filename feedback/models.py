from django.db import models


# Create your models here.

class Feedback(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    text = models.TextField(verbose_name='Отзыв')
    email = models.EmailField(verbose_name='Почта')
    is_confirmed = models.BooleanField(default=True, verbose_name='Подвержен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}: {self.email}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
