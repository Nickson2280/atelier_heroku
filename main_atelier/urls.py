from django.contrib import admin
from django.urls import path, include
from main_atelier.views import main

urlpatterns = [
    path('', main, name='main'),
]