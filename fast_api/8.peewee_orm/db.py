import os
from peewee import *

db = SqliteDatabase('db.sqlite3')

class Category(Model):
    code = CharField(unique=True)
    name = CharField()

    class Meta:
        database = db

class Product(Model):
    category = ForeignKeyField(Category, backref='products')
    code = CharField(max_length=30, unique=True)
    name = CharField(max_length=100)
    price = IntegerField()
    image_url = CharField(max_length=1000, null=True)

    class Meta:
        database = db

if not os.path.exists('db.sqlite3'):
    db.create_tables([Category, Product])