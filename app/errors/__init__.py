from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers # register error handlers with blueprint