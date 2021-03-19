from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')
    description = models.CharField(max_length=500, blank=True, verbose_name='Mô tả')
    price = models.IntegerField(verbose_name='Giá')

    def __str__(self):
        return self.name