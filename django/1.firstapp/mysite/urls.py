from django.contrib import admin
from django.urls import path

from .views import *  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # new
]
