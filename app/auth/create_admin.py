from app.database import db
from app.features.auth.model import User
from app.auth.roles import Roles
from app.config import AdminConfig
from werkzeug.security import generate_password_hash


def create_admin():
    if User.query.filter_by(username=AdminConfig.USER_ADMIN_USERNAME).first():
        return

    user = User(AdminConfig.USER_ADMIN_USERNAME,
                AdminConfig.USER_ADMIN_EMAIL,
                generate_password_hash(AdminConfig.USER_ADMIN_PASSWORD),
                Roles.ADMIN)
    db.session.add(user)
    db.session.commit()
    print('Admin creado')
