from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.auth.role_authenticate import role_authenticate
from app.auth.roles import Roles
from app.features.products.forms import FormProduct
from app.features.products.model import Product
from app.database import db


products_bp = Blueprint('products', __name__, template_folder='templates')


@products_bp.get('/products/')
@role_authenticate([Roles.ADMIN])
def index():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)

    print(page, per_page,)

    products = Product.query.paginate(
        page=page, per_page=per_page, error_out=False)

    context = {
        'pagination': products
    }

    return render_template('products.jinja2', **context)


@products_bp.get('/products/create/')
@role_authenticate([Roles.ADMIN])
def create():
    context = {
        'form': FormProduct(),
        'title': 'Crear Producto',
        'btn_text': 'Crear',
    }
    return render_template('form_product.jinja2', **context)


@products_bp.post('/products/create/')
@role_authenticate([Roles.ADMIN])
def create_product():

    form: FormProduct = FormProduct()
    context = {
        'form': form,
        'title': 'Crear Producto',
        'btn_text': 'Crear',
    }

    if not form.validate_on_submit():
        print(form.errors)
        return render_template('form_product.jinja2', **context)

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


@products_bp.get('/products/<int:id>/edit/')
@role_authenticate([Roles.ADMIN])
def edit(id):
    product = Product.query.get(id)
    form: FormProduct = FormProduct()

    if not product:
        flash("Producto no encontrado", 'error')
        return redirect(url_for('products.index'))

    form.name.data = product.name
    form.description.data = product.description
    form.price.data = product.price
    form.amount.data = product.amount
    form.category.data = product.category

    context = {
        'form': form,
        'title': 'Editar Producto',
        'btn_text': 'Editar',
    }
    return render_template('form_product.jinja2', **context)


@products_bp.post('/products/<int:id>/edit/')
@role_authenticate([Roles.ADMIN])
def edit_product(id):

    form: FormProduct = FormProduct()
    context = {
        'form': form,
        'title': 'Editar Producto',
        'btn_text': 'Editar',
    }

    if not form.validate_on_submit():
        print(form.errors)
        return render_template('form_product.jinja2', **context)

    try:
        product: Product = Product.query.get(id)
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.amount = form.amount.data
        product.category = form.category.data

        db.session.commit()
        return redirect(url_for('products.index'))
    except Exception as e:
        flash("Error al editar el producto", 'error')
        print(e)
        return redirect(url_for('products.edit', id=id))


@products_bp.get('/products/<int:id>/delete/')
@role_authenticate([Roles.ADMIN])
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.index'))
