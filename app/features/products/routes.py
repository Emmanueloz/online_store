from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.role_authenticate import role_authenticate
from app.auth.roles import Roles
products_bp = Blueprint('products', __name__, template_folder='templates')


@products_bp.get('/products/')
@role_authenticate([Roles.ADMIN])
def index():
    return render_template('products.jinja2')
