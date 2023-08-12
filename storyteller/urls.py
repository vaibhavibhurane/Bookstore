from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('second/index/', views.index, name='index'),
    path('third/', views.third, name='third'),
    path('third/data/', views.data, name='data'),
    path('third/index/', views.index, name='index'),
    path('storyteller/gallery/', views.gallery, name='gallery'),
    path('second/gallery/', views.gallery, name='gallery'),
    path('third/gallery/', views.gallery, name='gallery'),
    path('storyteller/about/', views.about, name='about'),
    path('second/about/', views.about, name='about'),
    path('third/about/', views.about, name='about'),
    path('data/', views.data, name='data'),
    path('data/purchase/', views.purchase, name='purchase'),
    path('data/purchase/order/', views.order, name='order'),
    path('purchase/index/', views.index, name='index'),
    path('purchase/about/', views.about, name='about'),
    path('purchase/gallery/', views.gallery, name='gallery'),
    path('data/index/', views.index, name='index'),
    path('data/gallery/', views.gallery, name='gallery'),
    path('data/about/', views.about, name='about'),
    path('data/add/', views.add, name='add'),
    path('data/add/addrecord/', views.addrecord, name='addrecord'),
    path('data/purchase/order/index/', views.index, name='index'),
    path('data/purchase/order/gallery/', views.gallery, name='gallery'),
    path('data/purchase/order/about/', views.about, name='about'),
]
