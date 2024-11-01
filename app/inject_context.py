from flask import Flask
from app.auth.roles import Roles


def inject_context(app: Flask):

    @app.context_processor
    def inject_current_user():
        return dict({
            'Roles': Roles,
        })

    return app
