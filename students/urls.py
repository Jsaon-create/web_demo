from django.urls import path
import students.views

urlpatterns = [
    path('', students.views.index),
    path('show/', students.views.show),
]