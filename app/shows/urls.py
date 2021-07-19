from django.contrib import admin
from django.urls import path
from . import views
from app.shows.views import *
app_name = 'shows'

urlpatterns = [
    # get list of most popular tv shows
    path('', views.index, name='index'),

    # filter list of tv shows by name
    path('show/<str:name>/', views.show_search, name='show_search'),

    # filter list of tv shows by releases date
    path('releases/<int:year>/', views.first_air_date_year, name='first_air_date_year'),

    # sort tv shows by popularity
    path('popularity/<str:popularity>/', views.popularity, name='popularity'),

    # allows to vote for the choosen tv show
    path('rating/', views.rating, name='rating'),
]
