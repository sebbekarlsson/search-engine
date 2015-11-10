from flask import Flask
from engine.models import Post
from .__init__ import config


app = Flask(__name__)

from .views.search import search
app.register_blueprint(search)


def run():
    app.run(
        threaded=True,
        debug=config['app']['debug'] or False,
        host=config['app']['host'] or '127.0.0.1'
    )