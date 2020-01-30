from django.db import models

class Author(models.Model):
   code = models.CharField(max_length=20, unique=True)
   name = models.CharField(max_length=50)

class Category(models.Model):
   code = models.CharField(max_length=20, unique=True)
   name = models.CharField(max_length=50)

class Book(models.Model):
   code = models.CharField(max_length=20, unique=True)
   name = models.CharField(max_length=50)
   author = models.ForeignKey(Author, on_delete=models.PROTECT)
   categories = models.ManyToManyField(Category)