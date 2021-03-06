from flask import Blueprint, render_template
from flask_security import current_user, login_required
from epic_win.products.models import Product

public = Blueprint('public', __name__)

@public.route('/')
def index():
    if current_user:
        print(current_user)
    items = Product.query.limit(5).all()
    return render_template("public/index.html", items=items)

@public.route('/about')
def about():
    return render_template("public/about.html")
