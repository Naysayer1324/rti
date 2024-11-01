from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:category_slug>/', views.CategoriesView.as_view(), name='categories'),
    path('goods/<slug:goods_slug>/', views.GoodsView.as_view(), name='goods')
]

