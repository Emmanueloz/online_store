from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.role_authenticate import role_authenticate
from app.features.products.model import Product

home_bp = Blueprint(
    'home', __name__, template_folder='templates', static_folder='public'
)


@home_bp.get('/')
def index():
    context = {
        'products': Product.query.all()
    }
    return render_template('index.jinja2', **context)


@home_bp.get('/category/<path:path>/')
def product_category(path):

    if path not in ['electrónicos', 'ropa', 'comida', 'juguetes', 'deportes', 'libros', 'música', 'computadoras',
                    'videojuego', 'otros']:
        flash("Categoría no encontrada", 'error')
        return redirect(url_for('home.index'))

    context = {
        'products': Product.query.filter(Product.category.like(path)).all(),
        'category': path
    }

    return render_template('index.jinja2', **context)
