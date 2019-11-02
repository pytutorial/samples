from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')
    description = models.CharField(max_length=500, blank=True, verbose_name='Mô tả')
    price = models.IntegerField(verbose_name='Giá')