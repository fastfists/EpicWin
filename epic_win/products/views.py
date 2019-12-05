from flask import Blueprint, render_template

views = Blueprint('products', __name__)

@views.route('/products')
def products():
    return render_template('products/single_item.html')
