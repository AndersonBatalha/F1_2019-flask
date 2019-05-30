from app.main import main
from flask import render_template

@main.errorhandler(401)
def not_authorized(e):
    return render_template('error/401.html', error=e, status_code=401), 401

@main.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', error=e, status_code=404), 404