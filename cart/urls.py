from django.urls import path
from .views import cart_details_view, add_to_cart_view, delete_from_cart_view

urlpatterns = [
    path('', cart_details_view, name='cart_details'),
    path('add/<int:product_id>', add_to_cart_view, name='cart_add'),
    path('delete/<int:product_id>', delete_from_cart_view, name='cart_delete'),
]
