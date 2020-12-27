from flask import render_template

from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return (
        render_template("404.html"),
        404,
    )  # Add error code number instead of default 200.


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # Ensure we don't effectuate faulty database changes.
    return render_template("500.html"), 500
