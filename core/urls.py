from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.user_register, name="register"),

    path('book_add/', views.book_add, name="book_add"),
    path('book/<str:pk>/', views.book_get, name="book_get"),
    path('book_filter/', views.book_filter, name="filter"),
    
    path('order_summary/', views.cart_get, name="order_summary"),
    path('cart_get/', views.cart_get, name="cart"),
    path('add_to_cart/', views.cart_add, name="add_to_cart"),
    path('subtract_from_cart/', views.cart_subtract, name="subtract_from_cart"),

]