from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.auth.role_authenticate import role_authenticate, current_user
from app.auth.roles import Roles
from app.features.products.model import Product
from app.features.orders.model import Order, OrderItem
from app.database import db
from app.features.orders.forms import OrderForm
from sqlalchemy import case

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

        print(list)
        listAmount = [int(i) for i in listAmount]
    except:
        flash("Error al procesar los pedidos", 'error')
        return redirect(url_for('home.index'))

    order_case = case(
        {id: index for index, id in enumerate(list)}, value=Product.id)

    listProducts = Product.query.filter(
        Product.id.in_(list)).order_by(order_case).all()

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

        order_case = case(
            {id: index for index, id in enumerate(list_ids)}, value=Product.id)

        list_products: list[Product] = Product.query.filter(
            Product.id.in_(list_ids)).order_by(order_case).all()

        list_unit_total = []
        for product, amount in zip(list_products, list_amount):
            list_unit_total.append(product.price * amount)
            product.amount -= amount
        total_order = sum(list_unit_total)

        db.session.commit()

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

    session['list_orders'] = [
        {'product': {
            'id': product.id,
            'name': product.name,
        }, 'amount': amount, 'total': unit_total}
        for product, amount, unit_total in zip(list_products, list_amount, list_unit_total)
    ]
    session['total_order'] = total_order

    return redirect(url_for('orders.payment_result'))


@orders_bp.get('/payment/success/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def payment_result():
    list_orders = session.get('list_orders', [])
    total_order = session.get('total_order', 0)

    print(list_orders)

    if not list_orders or not total_order:
        flash("No se encontraron pedidos", 'error')
        return redirect(url_for('home.index'))

    session.pop('list_orders', None)
    session.pop('total_order', None)

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


@orders_bp.get('/all/<int:id>/')
@role_authenticate([Roles.ADMIN])
def all_order(id):
    order = Order.query.filter(Order.id == id).first()

    if order is None:
        flash("No se encontró el pedido", 'error')
        return redirect(url_for('orders.all_orders'))

    form: OrderForm = OrderForm()
    form.state.data = order.state
    form.delivery_date.data = order.delivery_date
    context = {
        'order': order,
        'form': form
    }

    return render_template('order_details.jinja2', **context)


@orders_bp.post('/all/<int:id>/')
@role_authenticate([Roles.ADMIN])
def all_order_post(id):
    order: Order = Order.query.filter(Order.id == id).first()

    if order is None:
        print("No se encontró el pedido")
        flash("No se encontró el pedido", 'error')
        return redirect(url_for('orders.all_orders'))

    print(order)

    form: OrderForm = OrderForm()

    if not form.validate_on_submit():
        context = {
            'order': order,
            'form': form
        }

        return render_template('order_details.jinja2', **context)

    order.delivery_date = form.delivery_date.data
    order.state = form.state.data
    db.session.commit()
    flash("Se ha actualizado el pedido", 'success')
    return redirect(url_for('orders.all_orders'))


@orders_bp.get('/user/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def user_orders():
    orders = Order.query.filter(Order.user_id == current_user.id).all()
    context = {
        'orders': orders
    }
    return render_template('list_orders.jinja2', **context)


@orders_bp.get('/user/<int:id>/')
@role_authenticate([Roles.CLIENTE, Roles.ADMIN])
def user_order(id):
    order = Order.query.filter(Order.id == id).first()

    if order is None:
        flash("No se encontró el pedido", 'error')
        return redirect(url_for('orders.user_orders'))

    context = {
        'order': order,
    }

    return render_template('order_details.jinja2', **context)
