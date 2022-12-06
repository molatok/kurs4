from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    __table_args__ = {'extend_existing': True}
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    __table_args__ = {'extend_existing': True}
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'
    __table_args__ = {'extend_existing': True}
    title = Column(String(100), unique=False, nullable=False)
    description = Column(String(100), unique=False, nullable=False)
    trailer = Column(String(100), unique=False, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre. __tablename__}.id'), nullable=False)
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)


class User(models.Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(300), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    surname = Column(String(100), unique=True, nullable=False)
    favourite_genre = Column(Integer, ForeignKey(f'{Genre. __tablename__}.id'), nullable=False)
