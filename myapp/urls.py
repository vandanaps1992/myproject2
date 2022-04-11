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
    path('javascrpt/',views.javascrpt,name='javascrpt'),
    path('func/',views.func,name='func'),
    path('dommdl/',views.dommdl,name='dommdl'),
    path('evnodd/',views.evnodd,name='evnodd'),
    path('pattern/',views.pattern,name='pattern'),
    path('amstrong/',views.amstrong,name='amstrong'),
    path('palindrom/',views.palindrom,name='palindrom'),
    path('strpalndrom/',views.strpalndrom,name='strpalndrom'),
    path('validatn/',views.validatn,name='validatn'),
    path('calculator/',views.calculator,name='calculator'),
    path('newcalculator/',views.newcalculator,name='newcalculator')
]