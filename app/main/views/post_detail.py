from werkzeug.http import HTTP_STATUS_CODES

from app.models import Post
from app.main import main
from flask import render_template
from .errors import page_not_found

@main.route('/post/<slug>')
def post_detail(slug):
    p = Post.query.filter_by(slug=slug).first()
    if not p:
        return page_not_found(e=HTTP_STATUS_CODES[404])
    return render_template('post_detail.html', post=p)
