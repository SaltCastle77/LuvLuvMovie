from rest_framework import serializers
from .models import Movie, Genre, Review
from accounts.serializers import UserSerializer

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', )
    

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'backdrop_path',)

class MovieBackdropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'backdrop_path', )


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'user')
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(
        many = True,
        read_only=True,
    )
    genres = GenreListSerializer(
        many=True,
    )
    # like_users = serializers.StringRelatedField(many=True) 
    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'release_date', 'popularity',
            'overview', 'poster_path', 'backdrop_path', 'genres', 'where', 'review_set', 'like_users',)
