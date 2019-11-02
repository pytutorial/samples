from django.urls import path
from .views import *

urlpatterns = [
   path('hello', hello),
   path('products', getProducts),
   path('create_product', createProduct),
   path('update_product/<int:id>', updateProduct),
   path('delete_product/<int:id>', deleteProduct),
]