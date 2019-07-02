from app.main import main
from flask import render_template
from app.models import Post

@main.route('/')
def index():
    return render_template('index.html',
                           posts=Post.query.order_by(Post.data.desc()).all())
