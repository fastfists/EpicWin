from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, abort
from epic_win.ext import db
from flask_security import current_user, login_required
from .models import Product, PurchaseItem, Purchase
from sqlalchemy import or_
from .schemas import ProductSchema, SearchSchema, AddToCartSchema, ExecuuteSchema
import paypalrestsdk as paypal

views = Blueprint('products', __name__)

@views.route('/product/<string:slug>')
def single(slug):
    product = Product.query.filter(Product.slug == slug).first_or_404()
    similar_items = Product.query.filter(Product.product_type == product.product_type).filter(Product.id != product.id).paginate(page=1, per_page=3)

    context = {"product": product, "similar_items" : similar_items}
    return render_template('products/single_item.html', **context)

@views.route("/shop-finish")
@login_required
def execute_payment():

    schema = ExecuuteSchema()
    schema.load(request.args)
    pass

@views.route("/purchase", methods=["GET", "POST"])
@login_required
def purchase_cart():

    cart = current_user.get_cart()
    success, payment = create_invoice(cart)

    if not success:
        print(f'{ payment.error }')
        return abort(404)

    return_url = authorize_payment(payment)

    cart.is_checkout = False
    cart.payment_confirmation = payment.id

    db.session.add(cart)
    db.session.commit()

    return redirect(return_url)

def authorize_payment(payment):
    for link in payment.links:
        if link.rel == "approval_url":
            approval_url = str(link.href)
            return approval_url

def create_invoice(purchase:Purchase):

    purchase_dict = purchase.to_dict()

    payment = paypal.Payment({
        "intent": "sale",
        "payer": {
                "payment_method": "paypal"
            },
        "redirect_urls": {
            "return_url": f"{request.host_url}/shop-finish",
            "cancel_url": f"{request.host_url}/payments/error"
            },
        "transactions": [
            {
                "item_list": purchase_dict,
                "amount": {
                    "total": float(purchase.calc_total()),
                    "currency": "USD"
                    },
                "description": f"Epic Wins Sporting Goods"
            }]
        })

    success = payment.create()
    return success, payment

@views.route("/add-to-cart", methods=["GET", "POST"])
@login_required
def add_to_cart():

    schema = AddToCartSchema()
    body = schema.load(request.args)

    product = Product.query.filter(Product.slug == body.get("product")).first_or_404()
    item = PurchaseItem(product=product, count=body.get("quantity"))

    cart = current_user.get_cart() or Purchase(user=current_user, is_checkout=True)
    cart.items.append(item)

    db.session.add(cart)
    db.session.add(item)
    db.session.commit()

    flash("Added to cart")

    return redirect("/shop")

@views.route('/remove/<int:purchase_item_id>')
@login_required
def remove_item(purchase_item_id):

    item = PurchaseItem.query.filter(PurchaseItem.id ==  purchase_item_id).first_or_404()
    db.session.delete(item)
    db.session.commit()

    flash("Removed Item")

    return redirect("/checkout")

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

