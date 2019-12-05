from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name