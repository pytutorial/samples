from django.urls import path

from app.views import *

urlpatterns = [
    path('', index),
    path('hello', hello),
    path('hello/<name>', hello2),
]