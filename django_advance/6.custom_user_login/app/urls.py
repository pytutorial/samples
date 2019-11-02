from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', signup),
    path('', index, name='home')
]