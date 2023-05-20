from django.urls import path, include
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    path('login_user', views.login_user, name="login"),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name="logout"),

]
