from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    #Declare normal paths
]

#View set
router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls