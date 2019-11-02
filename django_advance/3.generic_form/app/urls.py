from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_product', ProductCreate.as_view(), name='product-create'),
    path('update_product/<pk>', ProductUpdate.as_view(), name='product-update'),
    path('delete_product/<int:id>', deleteProduct, name='product-delete')
]