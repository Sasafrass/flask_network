from flask import render_template

from app import app, db


@bp.app.errorhandler(404)
def not_found_error(error):
    return (
        render_template("errors/404.html"),
        404,
    )  # Add error code number instead of default 200.


@bp.app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # Ensure we don't effectuate faulty database changes.
    return render_template("errors/500.html"), 500
