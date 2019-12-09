from flask import Blueprint, render_template
from .schemas import Product

views = Blueprint('products', __name__)

@views.route('/shop')
def products():
    return render_template('products/index.html')

@views.route('/single')
def single():
    return render_template('products/single_item.html')


@views.route('/product', methods=["GET"])
@views.route('/product/<slug>', methods=["GET"])
def get_product():

    schema = ProductSchema()

    schema.dump(products)
