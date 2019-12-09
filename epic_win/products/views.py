from flask import Blueprint, render_template
from .models import Product

views = Blueprint('products', __name__)

@views.route('/products')
def products():
    items = Product.query.all()
    return render_template('products/index.html', items=items)

@views.route('/single')
def single():
    return render_template('products/single_item.html')
