# import json
from flask import Flask, render_template, request, jsonify
from functions import movie_title, movie_year, movie_rating, movie_genre, movie_actors, movie_category_and_year

app = Flask(__name__)


@app.route("/movie/<title>") # страничка фильмов по названиям
def movie_title_page(title):
    film = movie_title(title)
    return jsonify(film)

@app.route("/movie/years/<int:first_year>/<int:second_year>")  # страничка фильмов по годам
def movie_year_page(first_year, second_year):
    film = movie_year(first_year, second_year)
    return jsonify(film)

@app.route('movie/<rating>') # страничка фильмов по рейтингу
def movie_rating_page(rating):
    film = movie_rating(rating)
    return jsonify(film)

@app.route('movie/<genre>') # страничка фильмов по жанру
def movie_genre_page(genre):
    film = movie_genre(genre)
    return jsonify(film)

@app.route('movie/<first_actor>, <second_actor>') # страничка фильмов по актерам
def movie_actors_page(first_actor, second_actor):
    film = movie_actors(first_actor, second_actor)
    return jsonify(film)

@app.route('movie/<movie_type>, <int:release_year>, <genre>') # страничка фильмов по жанру, году
def movie_category_and_year_page(movie_type, release_year, genre):
    film = movie_category_and_year(movie_type, release_year, genre)
    return jsonify(film)

app.run()
