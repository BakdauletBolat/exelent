from django.db import models
from django.urls import reverse


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subTitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='SlideImages/')
    linkTo = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255)
    shortDescription = models.TextField()
    image = models.ImageField(upload_to="PageImages/")
    file = models.FileField(upload_to='PdfFile/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.id])

    def __str__(self):
        return self.title
