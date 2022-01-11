import sqlite3
import json


def movie_title(title):
    '''поиск по названию'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = "SELECT title, country, release_year, listed_in, description FROM netflix " \
                   f"WHERE title = {title}" \
                   f"ORDER BY release_year" \
                   f"LIMIT 1"
    cur = con.cursor()
    cur.execute(sqlite_query)
    movie = cur.fetchone()

    data = {
        "title": movie[0],
        "country": movie[1],
        "release_year": movie[2],
        "genre": movie[3],
        "description": movie[4]
    }

    con.close()
    return data


def movie_year(year1, year2):
    '''поиск по году выпуска'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = f"SELECT title, country, release_year, listed_in, description FROM netflix " \
                   f"WHERE release_year BETWEEN {year1} AND {year2}" \
                   f"LIMIT 100 "
    cur = con.cursor()
    cur.execute(sqlite_query)
    data = []
    for movie in cur.fetchone():
        films = {
            "title": movie[0],
            "country": movie[1],
            "release_year": movie[2],
            "genre": movie[3],
            "description": movie[4]
        }
        data.append(films)
    con.close()

    return data


def movie_rating(rating):
    '''поиск по рейтингу для детей'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = f"SELECT title, rating, description FROM netflix " \
                   f"WHERE rating = {rating}"
    cur = con.cursor()
    cur.execute(sqlite_query)
    data = cur.fetchone()

    data = {
        "title": data[0],
        "rating": data[1],
        "description": data[2]
    }
    con.close()
    return data


def movie_genre(genre):
    '''поиск по жанрам'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = f"SELECT title, rating, description FROM netflix " \
                   f"WHERE listed_in LIKE %{genre}%" \
                   f"LIMIT 10"
    cur = con.cursor()
    cur.execute(sqlite_query)
    data = []
    for movie in cur.fetchone():
        films = {
            "title": movie[0],
            "rating": movie[1],
            "description": movie[2]
        }
        data.append(films)
        con.close()

    return data


def movie_actors(first_actor, second_actor):
    '''поиск по актерам'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = f"SELECT 'cast' FROM netflix " \
                   f"WHERE 'cast' LIKE %{first_actor}% AND 'cast' LIKE %{first_actor}%"
    cur = con.cursor()
    cur.execute(sqlite_query)
    data = cur.fetchone()
    actors = data[0].split(', ')
    unique_actors = set(actors)
    unique_actors.remove(first_actor)
    unique_actors.remove(second_actor)

    return unique_actors


def movie_category_and_year(movie_type, release_year, genre):
    '''поиск по жанрам'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = f"SELECT title, release_year, rating, description, listed_in FROM netflix " \
                   f"WHERE type = {movie_type}" \
                   f"AND listed_in LIKE %{genre}%" \
                   f"AND release_year = {release_year}"
    cur = con.cursor()
    cur.execute(sqlite_query)
    data = []
    for movie in cur.fetchone():
        films = {
            "title": movie[0],
            "release_year": movie[1],
            "rating": movie[2],
            "description": movie[3],
            "listed_in": movie[4]
        }
        data.append(films)
        con.close()

    return data


def movies_all():
    '''все фильмы'''
    con = sqlite3.connect('netflix.db')
    sqlite_query = "SELECT * FROM netflix " \
                   "ORDER BY rating ASC " \
                   "LIMIT 100 OFFSET 100"
    cur = con.cursor()
    cur.execute(sqlite_query)
    movie = cur.fetchone()

    data = {
        "title": movie[0],
        "rating": movie[1],
        "country": movie[2],
        "release_year": movie[3],
        "genre": movie[4],
        "description": movie[5]
    }

    con.close()
    return data
