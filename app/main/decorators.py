from functools import wraps
from flask_login import current_user
from werkzeug.exceptions import HTTP_STATUS_CODES

from .views.errors import not_authorized


def tem_permissao(permissao, msg_erro):
    def decorador(f):
        @wraps(f)

        def permitir(*args, **kwargs):
            if current_user and (current_user.is_authenticated and not \
                    current_user.funcao.tem_permissao(permissao)):
                return not_authorized(e=msg_erro)

            return f(*args, **kwargs)
        return permitir

    return decorador
