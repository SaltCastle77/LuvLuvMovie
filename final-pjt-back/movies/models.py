from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='movies')
    where = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Review(models.Model):
    content = models.CharField(max_length=300)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_review')
