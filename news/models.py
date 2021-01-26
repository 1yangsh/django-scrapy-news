from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField('TITLE', max_length=300, help_text='news title')
    writer = models.CharField('WRITER', max_length=100, help_text='publisher')
    preview = models.TextField('PREVIEW', unique=True)

    def __str__(self):
        return self.title
