from flask import Flask
from app.config import Config
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.features.home import home_bp
    app.register_blueprint(home_bp)
    from app.features.auth import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context() as ctx:
        db.create_all()

    return app
