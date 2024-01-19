from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class PageContent(models.Model):
    title = models.CharField(max_length=20, default='Новая страница')
    header_name = models.CharField(max_length=20, default='СТРАНИЦА')
    url_name = models.CharField(max_length=20, unique=True, blank=True)
    body = RichTextUploadingField(default='Новая страница')

    def __str__(self):
        return self.title

