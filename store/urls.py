from django.urls import path
from .views import AddMovie, Home


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add/', AddMovie.as_view(), name='addmovie')
]