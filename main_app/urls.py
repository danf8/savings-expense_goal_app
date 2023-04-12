from django.urls import path
from . import views

urlpatterns= [
    path('', views.home),
    path('about/', views.about),
    path('savings/', views.savings, name='savings_index'),
]