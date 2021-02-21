import random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Genre, Movie, Review
from .serializers import (
    GenreListSerializer,
    MovieListSerializer,
    MovieSerializer,
    MovieBackdropSerializer,
    ReviewSerializer
)


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request, genre_pk):
    # print(genre_pk)
    movies = Movie.objects.all().filter(genres__id__icontains=genre_pk).order_by('-vote_average')[:10]
    serializer = MovieListSerializer(movies, many=True)
    # print('clear')
    return Response(serializer.data)


@api_view(['GET'])
def movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_category(request, where):
    movies = Movie.objects.all().filter(where=where).order_by('-vote_average')[:10]
    serializer = MovieListSerializer(movies, many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.pk).exists():
            return Response(True)
        else:
            return Response(False)
    else:
        if movie.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소
            movie.like_users.remove(request.user)
            return Response({'like': False})
        else:
            # 좋아요
            movie.like_users.add(request.user)
            return Response({'like': True})


# 리뷰 작성, 리뷰 리스트
@api_view(['POST', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data) 


# 내가 좋아요한 영화들
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie(request):
    movies = request.user.like_movies
    # movies = Movie.objects.all()
    # print(request.method)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    movies = request.user.like_movies.all()
    genres = dict()
    for movie in movies:
        for g in movie.genres.all():
            # print(g)
            if g.name in genres:
                val = genres[g.id]
                genres[g.id] = val + 1
            else:
                genres[g.id] = 1
    # print(genres)
    max_v = max_g = 0
    for (key, val) in genres.items():
        if val > max_v:
            max_g = key
            max_v = val

    
    movies = Movie.objects.all().filter(genres__id__icontains=max_g).order_by('-vote_average')[:10]
    serializer = MovieListSerializer(movies, many=True)
    
    return Response(serializer.data)