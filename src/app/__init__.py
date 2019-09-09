""" App entry point. """
import os
from sanic import Sanic
from sanic_cors import CORS
from sanic.response import text, json

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')


def create_app():
    """ Function for bootstrapping sanic app. """
    app = Sanic(__name__)
    app.static('/static', STATIC_FOLDER)
    app.static('/favicon.ico', os.path.join(STATIC_FOLDER, 'img', 'favicon.ico'))
    CORS(app, automatic_options=True, supports_credentials=True,
         origins="http://localhost:3000")
