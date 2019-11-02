from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('page1', page1, name='page-1'),
    path('page2', page2, name='page-2')
]