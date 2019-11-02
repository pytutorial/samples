from django.urls import path
from rest_framework_simplejwt import views as jwt_views 

from .views import *

urlpatterns = [    
    path('api/token', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view()),
    path('create_user', createUser),
    path('products',  getProducts),
]