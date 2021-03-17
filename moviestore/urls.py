from django.urls import path
from .views import MovieList, MovieDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('', views.index),
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)