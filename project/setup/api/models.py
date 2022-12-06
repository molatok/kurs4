from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарковский'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Самый лучший фильм'),
    'description': fields.String(required=True, max_length=250, example='Я не знаю, что сказать'),
    'trailer': fields.String(required=True, max_length=100, example='Я не знаю, что сказать'),
    'year':fields.Integer(required=True, example=2022),
    'rating': fields.Float(required=True, example=10.0),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=200, example='mail@example.com'),
    'password': fields.String(required=True, max_length=200, example='12345678'),
    'name': fields.String(required=True, max_length=200, example='Иван'),
    'surname': fields.String(required=True, max_length=200, example='Иванов'),
    'genre': fields.Nested(genre)
})