from app import app, db
from app.models import User, Post


@app.shell_context_processors
def make_shell_contex():
    return {'db': db, 'User': User, 'Post': Post}