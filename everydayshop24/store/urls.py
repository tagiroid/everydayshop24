from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    path('', views.store, name="store"),
    path('registration/login/', views.login, name='login'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]
