from django.contrib import admin
from django.urls import path
from . import views
from app.movies.views import *
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    # path('movie/create/',movie_create.as_view(), name='movie_create'),
    # #
    # path('movie/list/',movie_list.as_view(), name='movie_list'),
    # #
    # path('movie/update/<int:pk>/',movie_update.as_view(), name='movie_update'),
    # #
    # path('movie/delete/<int:pk>/',movie_delete.as_view(), name='movie_delete'),
    # #
    # path('movie/detail/<int:pk>/',movie_detail.as_view(), name='movie_detail'),
]
