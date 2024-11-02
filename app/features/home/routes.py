from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.role_authenticate import role_authenticate
from app.auth.roles import Roles
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


@home_bp.get('/orders/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def orders():
    try:
        list = request.args.get("list", []).split(",")
        listAmount = request.args.get("amount", []).split(",")

        if not list:
            flash("No hay pedidos", 'error')
            return redirect(url_for('home.index'))

        list = [int(i) for i in list]
        listAmount = [int(i) for i in listAmount]
    except:
        flash("Error al procesar los pedidos", 'error')
        return redirect(url_for('home.index'))

    listProducts = Product.query.filter(Product.id.in_(list)).all()

    listUnitTotal = []

    for product, amount in zip(listProducts, listAmount):
        listUnitTotal.append(product.price * amount)

    listOrders = zip(listProducts, listAmount, listUnitTotal)
    totalOrder = sum(listUnitTotal)

    context = {
        'orders': listOrders,
        "totalOrder": totalOrder,
    }

    return render_template('order.jinja2', **context)
