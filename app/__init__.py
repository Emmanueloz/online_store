from flask import Flask
from app.config import Config
from app.database import db, migrate
from app.auth import login_manager
from app.auth.create_admin import create_admin
from app.inject_context import inject_context


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app = inject_context(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.features.home import home_bp
    app.register_blueprint(home_bp)
    from app.features.auth import auth_bp
    app.register_blueprint(auth_bp)
    from app.features.products import products_bp
    app.register_blueprint(products_bp)
    from app.features.orders import orders_bp
    app.register_blueprint(orders_bp)

    with app.app_context() as ctx:
        db.create_all()
        create_admin()

    return app
