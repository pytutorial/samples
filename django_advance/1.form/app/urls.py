from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_product', createProduct, name='product-create'),
    path('update_product/<int:id>', updateProduct, name='product-update'),
    path('delete_product/<int:id>', deleteProduct, name='product-delete')
]