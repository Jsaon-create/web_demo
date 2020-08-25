from django.contrib import admin
from django.urls import path
from house import views

urlpatterns = [
    path('', views.house_info)
]
