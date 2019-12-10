from flask import Blueprint, render_template, request, jsonify
from .models import Product
from .schemas import ProductSchema, SearchSchema

views = Blueprint('products', __name__)

@views.route('/shop')
def products():
    return render_template('products/index.html')

@views.route('/single')
def single():
    return render_template('products/single_item.html')

@views.route('/v1/product/<string:slug>', methods=["GET"])
def get_product(slug):
    schema = ProductSchema()
    product = Product.query.filter(Product.slug == slug).first_or_404()
    return schema.dump(product)

@views.route('/v1/search')
def search():
    """
    page = 1
    """
    schema = SearchSchema()
    body = schema.load(request.args)
    query = Product.query

    data = query.paginate(page=body.get("page"), per_page=body.get("per_page"), error_out=False)
    return jsonify({"products": ProductSchema(many=True).dump(data.items)})

