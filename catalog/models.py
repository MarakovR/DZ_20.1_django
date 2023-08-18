from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    picture = models.ImageField(verbose_name='изображение')
    category = models.ForeignKey('category', on_delete=models.PROTECT, null=True, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_of_creation = models.DateTimeField(verbose_name='дата создания')
    date_changes = models.DateTimeField(verbose_name='дата изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
