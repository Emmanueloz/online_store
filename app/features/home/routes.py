from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.get('/')
def index():
    return render_template('index.jinja2')