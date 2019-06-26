from app.models import Post
from app.main import main
from flask import render_template

@main.route('/posts')
def posts():
    posts = Post.query.order_by( Post.data.date(), Post.data.time() ).all()
    return render_template('posts.html', posts=posts)
