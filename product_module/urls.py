from django.urls import path
from .views import trial,index, cart, removecart, success_page, error_page

urlpatterns = [
    path('', trial),
    path('index/', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
]