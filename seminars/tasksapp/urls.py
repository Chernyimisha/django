from django.urls import path
from . import views

urlpatterns = [
    path('task1/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about me'),
    path('throws/', views.throws, name='throws'),
    path('values/', views.throws_values, name='throws_values'),
]