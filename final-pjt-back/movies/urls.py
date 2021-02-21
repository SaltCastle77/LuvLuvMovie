from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/movielist/<int:genre_pk>/', views.movie_list),
    path('category/<str:where>/', views.movie_category),
    path('<int:movie_pk>/', views.movie),
    path('<int:movie_pk>/like/', views.like),
    path('<int:movie_pk>/reviews/', views.review_list_create),
    path('mymovies/', views.my_movie),
    path('recommend/', views.recommend),
]
