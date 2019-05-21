from app.main import main
from flask import render_template

@main.errorhandler(401)
def not_authorized(e):
    print(e)
    return render_template('401.html', error=e, status_code=401), 401

@main.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html', error=e, status_code=401), 404