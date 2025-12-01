from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.signup_view, name='signup'),  # add signup route
]
