from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

# Add vars for flask shell env
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
