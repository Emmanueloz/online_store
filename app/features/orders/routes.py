from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.role_authenticate import role_authenticate
from app.auth.roles import Roles
from app.features.products.model import Product


orders_bp = Blueprint('orders', __name__,
                      template_folder='templates', url_prefix='/orders/', static_folder='public')


@orders_bp.get('/')
@role_authenticate([Roles.ADMIN, Roles.CLIENTE])
def index():
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


@orders_bp.get('/my-orders/')
def my_orders():
    context = {
        "orders": []
    }
    return render_template('index_orders.jinja2', **context)


@orders_bp.get('/payment/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def payment():

    return render_template('payment.jinja2')
