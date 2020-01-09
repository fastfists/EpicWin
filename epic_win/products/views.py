from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from .models import Product
from sqlalchemy import or_
from .schemas import ProductSchema, SearchSchema

views = Blueprint('products', __name__)

@views.route('/shop')
def products():
    return render_template('products/index.html')

@views.route('/product/<string:slug>')
def single(slug):
    product = Product.query.filter(Product.slug == slug).first_or_404()
    return render_template('products/single_item.html', product=product)

@views.route('/search', methods=["GET", "POST"])
def search_form():
    print(request.args)
    q = request.args.get("search", None)
    print(q)
    if q:
        return redirect(f"/shop?q={q}")
    else:
        return redirect(f"/shop")

@views.route('/api/v1/product/<string:slug>', methods=["GET"])
def get_product(slug):
    schema = ProductSchema()
    product = Product.query.filter(Product.slug == slug).first_or_404()
    return schema.dump(product)

@views.route('/api/v1/search')
def search():
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

    if body.get("max"):
        max_price = body.get("max")
        query = query.filter(Product.cost <= max_price)

    if body.get("max"):
        max_price = body.get("max")
        query = query.filter(Product.cost <= max_price)

    if body.get("type"):
        product_type = body.get("type")
        query = query.filter(Product.product_type == product_type)

    if body.get("q"):
        q = body.get("q")
        tokens = q.split(' ')
        query = query.filter(or_(Product.name.ilike(f"%{token}%") for token in tokens))

    data = query.paginate(page=body.get("page"), per_page=body.get("per_page"), error_out=False)
    return jsonify({"products": ProductSchema(many=True).dump(data.items), "pages" : data.pages, "total" : data.total })

@views.route('/checkout')
def checkout():
    return render_template("products/checkout.html")
