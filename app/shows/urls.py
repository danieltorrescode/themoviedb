from django.contrib import admin
from django.urls import path
from . import views
from app.shows.views import *
app_name = 'shows'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<str:name>/', views.show_search, name='show_search'),
    path('releases/<int:year>/', views.first_air_date_year, name='first_air_date_year'),
    path('popularity/<str:popularity>/', views.popularity, name='popularity'),
    path('rating/', views.rating_show),
]
