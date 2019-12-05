from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create_product', createProduct)
]