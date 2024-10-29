from django.contrib import admin
from django.urls import path, include

from goods import views

app_name = 'goods'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog')
]