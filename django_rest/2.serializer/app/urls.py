from django.urls import path
from .views import *

urlpatterns = [
   path('products', getProducts),
   path('create_product', createProduct),
   path('update_product/<int:id>', updateProduct),
   path('update_product_partial/<int:id>', updateProductPartial),
   path('delete_product/<int:id>', deleteProduct),
]