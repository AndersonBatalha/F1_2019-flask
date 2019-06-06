from ..forms import PostForm
from app.main import main
from flask import render_template, request, flash
from .upload_file import allowed_extension, upload

@main.route('/add_post', methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        if request.method == "POST":
            if allowed_extension(request.files['imagem'].filename):
                upload()
                flash('Postagem adicionada', category='success')
            else:
                flash('Apenas arquivos de imagem são válidos', category='warning')

    return render_template('forms/add_post.html', form=form)