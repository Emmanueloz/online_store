from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.role_authenticate import role_authenticate
from app.auth.roles import Roles
from app.features.products.forms import FormProduct
from app.features.products.model import Product
from app.database import db


products_bp = Blueprint('products', __name__, template_folder='templates')


@products_bp.get('/products/')
@role_authenticate([Roles.ADMIN])
def index():

    context = {
        'products': Product.query.all()
    }

    return render_template('products.jinja2', **context)


@products_bp.get('/products/create/')
@role_authenticate([Roles.ADMIN])
def create():
    context = {
        'form': FormProduct()
    }
    return render_template('create_product.jinja2', **context)


@products_bp.post('/products/create/')
@role_authenticate([Roles.ADMIN])
def create_product():

    form: FormProduct = FormProduct()
    context = {
        'form': form
    }

    if not form.validate_on_submit():
        print(form.errors)
        return render_template('create_product.jinja2', **context)

    try:
        product = Product(form.name.data, form.description.data,
                          form.price.data, form.amount.data, form.category.data)

        db.session.add(product)
        db.session.commit()

        return redirect(url_for('products.index'))
    except Exception as e:
        flash("Error al crear el producto", 'error')
        print(e)
        return redirect(url_for('products.create'))


@products_bp.get('/products/<int:id>/delete/')
@role_authenticate([Roles.ADMIN])
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))
