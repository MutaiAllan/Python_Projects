from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))

    genre = relationship('Genre', back_populates='movies')
    director = relationship('Director', back_populates='movies')

Genre.movies = relationship('Movie', back_populates='genre')
Director.movies = relationship('Movie', back_populates='director')
