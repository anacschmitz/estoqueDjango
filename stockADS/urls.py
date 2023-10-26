from django.urls import path
from . import views

urlpatterns = [
  path('inicio/', views.index, name='home'),
  path('add-product/',views.add_product, name='add-product'),
  path('product-detail/<int:id>', views.product_detail, name='product-detail'),
  path('delete-product/<int:id>', views.delete_product, name='delete-product')
]