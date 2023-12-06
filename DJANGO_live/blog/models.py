from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Post title')
    text = models.TextField()
    tag = models.CharField(max_length=255)
    published = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['title', 'update_date']

    def __str__(self):
        return f'{self.title} - {self.create_date}'
