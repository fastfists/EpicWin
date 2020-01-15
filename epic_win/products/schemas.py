from .models import Product
from epic_win.ext import ma
from marshmallow import fields


class ProductSchema(ma.ModelSchema):

    cost = fields.Float()
    class Meta:
        model = Product
        exclude = ("id",)

class SearchSchema(ma.Schema):

    page = fields.Integer(default=1)
    per_page = fields.Integer(default=12)
    max = fields.Decimal()
    min = fields.Decimal()
    type = fields.String()
    q = fields.String()

    def __repr__(self):
        return self.page

class AddToCartSchema(ma.Schema):

    product = fields.String()
    quantity = fields.Integer()

class ExecuteSchema(ma.Schema):

    paymentId = fields.String()
    token = fields.String()
    PayerID = fields.String()
