"""Restoranti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from produktet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('browse/', views.browse),
    path('filter/', views.filter),
    path('login/', views.login_method),
    path('register/', views.register_method),
    path('restaurant/', views.home_page),
    path('addtocart/', views.buy_now),
    path('cart/', views.purchuases),
    path('delete/', views.delete),
    path('check/',views.check_out),
    path('log/', views.logout_user),
    path('srch/', views.search),
    path('about/', views.aboutus)
]
