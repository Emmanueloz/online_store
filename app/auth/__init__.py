from flask_login import LoginManager
from app.features.auth.model import User
from app.auth.user import UserLogin
from app.auth.roles import Roles
from app.auth.role_authenticate import role_authenticate

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None

    user: User = User.query.get(user_id)

    if user is None:
        return None

    return UserLogin(user.id, user.username, user.email, user.password)
