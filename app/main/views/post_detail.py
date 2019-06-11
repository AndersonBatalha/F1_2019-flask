from app.models import Post
from app.main import main
from flask import render_template

@main.route('/post/<slug>')
def post_detail(slug):
    p = Post.query.filter_by(slug=slug).first()
    return render_template('post_detail.html', post=p)
