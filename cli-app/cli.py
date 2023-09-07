import click
from database import SessionLocal, engine
from models import Movie, Genre, Director, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('genre')
@click.argument('director')
def add_movie(title, genre, director):
    """Add a new movie."""
    db = SessionLocal()
    genre_obj = db.query(Genre).filter_by(name=genre).first()
    if not genre_obj:
        genre_obj = Genre(name=genre)
        db.add(genre_obj)

    director_obj = db.query(Director).filter_by(name=director).first()
    if not director_obj:
        director_obj = Director(name=director)
        db.add(director_obj)

    movie = Movie(title=title, genre=genre_obj, director=director_obj)
    db.add(movie)
    db.commit()
    db.close()
    click.echo("Movie added successfully!")

@cli.command()
def list_movies():
    """List all movies."""
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()
    if not movies:
        click.echo("No movies found.")
    else:
        for movie in movies:
            click.echo(f"{movie.title} - Genre: {movie.genre.name}, Director: {movie.director.name}")

# Add more commands for updating and deleting movies if needed

if __name__ == '__main__':
    cli()
