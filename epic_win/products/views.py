from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from .models import Product
from sqlalchemy import or_
from .schemas import ProductSchema, SearchSchema

views = Blueprint('products', __name__)

@views.route('/product/<string:slug>')
def single(slug):
    product = Product.query.filter(Product.slug == slug).first_or_404()
    return render_template('products/single_item.html', product=product)

@views.route('/search', methods=["GET", "POST"])
def search_form():
    print(request.form)
    q = request.form.get("search", None)
    print(q)
    if q:
        return redirect(f"/shop?q={q}")
    else:
        return redirect(f"/shop")


@views.route('/shop')
def products():
    """
        page = 1
        per_page=12
        max=160
        min=100
        type (category)
        q=None (query string)
    """
    schema = SearchSchema()
    body = schema.load(request.args)
    query = Product.query

    if body.get("min"):
        min_price = body.get("min")
        query = query.filter(Product.cost <= min_price)

    if body.get("max"):
        max_price = body.get("max")
        query = query.filter(Product.cost >= max_price)

    if body.get("type"):
        product_type = body.get("type")
        query = query.filter(Product.product_type == product_type)

    if body.get("q"):
        q = body.get("q")
        tokens = q.split(' ')
        query = query.filter(or_(Product.name.ilike(f"%{token}%") for token in tokens))

    data = query.paginate(page=body.get("page"), per_page=12, error_out=False)
    context = { "pagination" : data, "q" : body.get("q") }

    return render_template('products/index.html', **context)

@views.route('/checkout')
def checkout():
    return render_template("products/checkout.html")
