from django.urls import path
# from .views import MovieList, MovieDetail, UserDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns
from moviestore.views import MovieViewSet, UserViewSet
from rest_framework import renderers

movie_list = MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
movie_detail = MovieViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    # path('', views.index),
    path('movies/', movie_list, name="movie-list"),
    path('movies/<int:pk>', movie_detail, name="movie-detail"),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)