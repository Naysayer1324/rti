from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='category_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    power = models.CharField(max_length=150, verbose_name='Мощность')
    acceleration = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, verbose_name='Разгон')
    consumption = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, verbose_name='Расход')
    emissions = models.IntegerField(verbose_name='Выбросы')
    category = models.ForeignKey(to=Categories, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'goods'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('goods:product', kwargs={'product_slug': self.slug})
