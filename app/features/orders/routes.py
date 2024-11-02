from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.role_authenticate import role_authenticate, current_user
from app.auth.roles import Roles
from app.features.products.model import Product
from app.features.orders.model import Order, OrderItem
from app.database import db

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
        'listOrders': list,
        'listAmount': listAmount,
        'totalOrder': totalOrder,
    }

    return render_template('order.jinja2', **context)


@orders_bp.get('/payment/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def payment():
    try:
        list_ids = request.args.getlist("list")
        list_amount = request.args.getlist("amount")

        list_ids = [int(i) for i in list_ids]
        list_amount = [int(i) for i in list_amount]

        list_products: list[Product] = Product.query.filter(
            Product.id.in_(list_ids)).all()

        list_unit_total = []
        for product, amount in zip(list_products, list_amount):
            list_unit_total.append(product.price * amount)
            product.amount -= amount
        db.session.commit()

        total_order = sum(list_unit_total)

        order: Order = Order(current_user.id, 'pending', total_order)
        db.session.add(order)
        db.session.commit()

        for product, amount in zip(list_products, list_amount):
            order_item = OrderItem(order.id, product.id, amount, product.price)
            db.session.add(order_item)
            db.session.commit()

    except Exception as e:
        print(e)
        flash("Error al procesar los pedidos", 'error')
        return redirect(url_for('home.index'))

    list_orders = zip(list_products, list_amount, list_unit_total)

    context = {
        'list_orders': list_orders,
        'total_order': total_order,
    }
    return render_template('payment.jinja2', **context)


@orders_bp.get('/all/')
@role_authenticate([Roles.ADMIN])
def all_orders():
    orders = Order.query.all()
    context = {
        'orders': orders
    }

    return render_template('list_orders.jinja2', **context)
