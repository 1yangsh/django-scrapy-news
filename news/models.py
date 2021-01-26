from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField('TITLE', max_length=300, help_text='news title')
    writer = models.CharField('WRITER', max_length=100, help_text='publisher')
    preview = models.TextField('PREVIEW', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
        db_table = 'news_new'

    def get_absolute_url(self):
        # -> 1st post -> /blog/post/1st-post
        return reverse('news:news_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
