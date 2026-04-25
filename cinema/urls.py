from django.urls import path

from cinema.views import MoviesList, MovieDetail

urlpatterns = [
    path("movies/", MoviesList.as_view(), name="movies-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]
