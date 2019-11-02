from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),                 # new
    path('accounts/signup', signup),                                        # new
]