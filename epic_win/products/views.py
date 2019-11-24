from flask import Blueprint, render_template

views = Blueprint('products', __name__)

@views.route('/products')
def products():
    pass
