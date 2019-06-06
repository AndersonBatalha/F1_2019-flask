from werkzeug.utils import secure_filename
import app, os
from app.main import main
from flask import request, flash, redirect

def allowed_extension(filename):
    return ('.' in filename) and (filename.split('.')[1].lower() in app.config.ALLOWED_EXTENSIONS)

@main.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'imagem' not in request.files:
            flash("Erro! Imagem não enviada")
            return redirect(request.url)
        img = request.files['imagem']
        if img.filename == "":
            flash("Nenhuma imagem selecionada")
            return redirect(request.url)
        if img and allowed_extension(img.filename):
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config.UPLOAD_FOLDER, filename))