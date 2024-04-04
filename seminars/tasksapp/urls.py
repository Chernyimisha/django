from django.urls import path
from . import views

urlpatterns = [
    path('task1/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about me'),
    path('throws/', views.throws, name='throws'),
    path('bones/', views.bones, name='bones'),
    path('numbers/', views.numbers, name='randnumber'),
    path('values/', views.throws_values, name='throws_values'),
    path('index/', views.get_index, name='get_index'),
    path('about2/', views.get_about, name='get_about'),
    path('game/', views.game_forms, name='game_forms'),
]

