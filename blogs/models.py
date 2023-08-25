from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(verbose_name='содержимое')

    picture = models.ImageField(null=True, verbose_name='изображение')
    date_of_creation = models.DateTimeField(null=True, verbose_name='дата создания')
    slug = models.CharField(null=True, blank=True, max_length=150, verbose_name='slug')
    publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
