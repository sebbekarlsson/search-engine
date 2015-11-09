from flask import Flask
from engine.models import Post


app = Flask(__name__)

from .views.search import search
app.register_blueprint(search)


def run():
    app.run(threaded=True, debug=True)