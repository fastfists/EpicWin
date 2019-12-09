from .models import Product
from epic_win.ext import ma

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product

