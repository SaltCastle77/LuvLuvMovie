import requests
import os
from tmdb import TMDB_URL_Maker
import json


tmdb = TMDB_URL_Maker()

def get_genre():
    url = tmdb.get_url('genre/movie/list')
    payload = {
        'api_key': tmdb.api_key,
        'language': tmdb.language,
    }
    res = requests.get(url, params=payload)
    res.encoding = 'ISO-639-1'
    res_result = res.json().get('genres')
    genre_res = []
    for genre in res_result:
        genre_data = {
            "model": "movies.genre",
            "pk": genre.get('id'),
            "fields": {
                "name": genre.get('name')
            }
            }
        genre_res.append(genre_data)

    with open('shared/data/genre.json', 'w', encoding='UTF8') as json_file:
        json.dump(genre_res, json_file, ensure_ascii=False, indent='\t')


def get_movies(q):
    url = tmdb.get_url(f'movie/{q}/')

    payload = {
        'api_key': tmdb.api_key,
        'language': tmdb.language,
        'page': 1
    }
    movie_res = []
    for i in range(1, 11):
        payload['page'] = i
        # print(payload['page'])
        res = requests.get(url, params=payload)
        res.encoding = 'ISO-639-1'
        res_result = res.json().get('results')
        for movie in res_result:
            # print(str(movie.get('backdrop_path')  or '' ))
            movie_data = {
                "model": "movies.movie",
                "pk": movie.get('id'),
                "fields": {
                    "title": movie.get('title'),
                    "original_title": movie.get('original_title'),
                    "release_date": movie.get('release_date'),
                    "popularity": movie.get('popularity'),
                    "vote_count": movie.get('vote_count'),
                    "vote_average": movie.get('vote_average'),
                    "overview": movie.get('overview'),
                    "poster_path": 'https://image.tmdb.org/t/p/w1280' + str(movie.get('poster_path') or ''),
                    "backdrop_path": 'https://image.tmdb.org/t/p/w1280' + str(movie.get('backdrop_path') or ''),
                    "genres": movie.get('genre_ids'),
                    "where": q
                }
            }
            movie_res.append(movie_data)

        with open(f'shared/data/{q}.json', 'w', encoding='UTF8') as json_file:
            json.dump(movie_res, json_file, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    # get_movies('top_rated')
    get_movies('popular')
    # get_movies('now_playing')
    # get_genre()
