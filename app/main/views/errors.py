from app.main import main
from flask import render_template

@main.errorhandler(500)
def not_authorized(e):
    print(e)
    return render_template('500.html', error=e, status_code=500), 500

@main.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html', error=e, status_code=404), 404