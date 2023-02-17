from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
