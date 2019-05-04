from django.urls import path

from . import views

urlpattenrns = [
    path('',views.index, name ='index'),
]