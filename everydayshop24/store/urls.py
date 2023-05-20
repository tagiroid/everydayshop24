from django.urls import path, include
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    path('', views.store, name="store"),
    path('authentication/login/', views.login, name='login'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('authentication/', include('authentication.urls')),
]
