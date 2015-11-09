from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from ..session import sess
from engine.models import Post


search = Blueprint('search', __name__,
                        template_folder='templates')

@search.route('/')
def _search():
    posts = sess.query(Post)
    return render_template('search.html', posts=posts)