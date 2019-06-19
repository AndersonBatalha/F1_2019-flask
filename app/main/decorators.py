import functools
from flask_login import current_user
from werkzeug.exceptions import HTTP_STATUS_CODES

from .views.errors import not_authorized


def admin_required(f):
    """Verifica se o usuário está logado. Caso esteja, verifica se este é administrador."""
    @functools.wraps(f)
    def is_admin(*args, **kwargs):
        if current_user and (current_user.is_authenticated and not \
                current_user.funcao.nome_funcao.startswith('Adm')):
            return not_authorized(HTTP_STATUS_CODES[401])

        return f(*args, **kwargs)

    return is_admin
