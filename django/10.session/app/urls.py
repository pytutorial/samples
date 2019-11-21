from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('page2', page2, name='page2')
]