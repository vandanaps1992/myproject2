from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path('home/',views.home,name='home'),
    path('new/',views.new,name='new'),
    path('grid/',views.grid,name='grid'),
    path('products/',views.products,name='products'),
    path('newpage/',views.newpage,name='newpage'),
    path('productsnew/',views.productsnew,name='productsnew'),
    path('javascrpt/',views.javascrpt,name='javascrpt')
]