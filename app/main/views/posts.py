from app.models import Post
from app.main import main
from flask import render_template

@main.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)
