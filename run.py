from project.config import config
from project.models.models import Genre, Movie, User, Director
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Movie": Movie,
        "User": User,
        "Director": Director
    }

if __name__ == '__main__':
    app.run(
        host = "localhost",
        port=8080,
        debug=True
    )
