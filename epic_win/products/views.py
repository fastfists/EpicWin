from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from epic_win.ext import db
from flask_security import current_user, login_required
from .models import Product, PurchaseItem, Purchase
from sqlalchemy import or_
from .schemas import ProductSchema, SearchSchema, AddToCartSchema

views = Blueprint('products', __name__)

@views.route('/product/<string:slug>')
def single(slug):
    product = Product.query.filter(Product.slug == slug).first_or_404()
    similar_items = Product.query.filter(Product.product_type == product.product_type).filter(Product.id != product.id).paginate(page=1, per_page=3)

    context = {"product": product, "similar_items" : similar_items}
    return render_template('products/single_item.html', **context)

@views.route("/add-to-cart", methods=["GET", "POST"])
@login_required
def add_to_cart():

    product = Product.query.filter(Product.slug == body.get("product")).first_or_404()
    item = PurchaseItem(product=product, count=body.get("quantity"))

    cart = current_user.get_cart() or Purchase(user=current_user, is_checkout=True)
    cart.items.append(item)

    db.session.add(cart)
    db.session.add(item)
    db.session.commit()
    flash("Added to cart")

    return redirect("/shop")

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
        query = query.filter(Product.cost >= min_price)

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

    data = query.paginate(page=body.get("page"), per_page=12, error_out=False)

    categories = ["Nike",
                  "UnderArmour",
                  "Epic Wins",
                  "Camping/Hiking",
                  "Cowboys",
                  "Hunting Gear",
                  "Cycling/Biking",
                  "Fishing",
                  "Winter Sports",
                  "Baltimore Raven"]

    context = { "pagination" : data, "q" : body.get("q"), "categories" : categories }

    return render_template('products/index.html', **context)

@views.route('/checkout')
@login_required
def checkout():

    return render_template("products/checkout.html", cart=current_user.get_cart())



