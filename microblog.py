from app import app, db, cli
from app.models import Post, User


# Add vars for flask shell env
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
