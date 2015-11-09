from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from ..session import sess
from engine.models import Post
from flask.ext.wtf import Form
from wtforms import TextField


search = Blueprint('search', __name__,
                        template_folder='templates')

class SearchForm(Form):
    q = TextField('Search')

@search.route('/search', methods=['POST', 'GET'])
def _search():
    form = SearchForm(request.form, csrf_enabled=False)

    posts = None

    term = request.args.get('q')
    if term is not None and term is not '':
        posts = sess.query(Post).filter(Post.content.like('%' + term + '%'), Post.type=='post')
        print(term)

    
    return render_template('search.html', form=form, posts=posts)