from .models import *
from epic_win.ext import admin, db
from epic_win.admin import CustomView

def init_admin():
    tables = [Discount, Purchase, PurchaseItem, OrderOption, Coupon, Reviews]
    admin.add_view(CustomView(ProductView, db.session))
    for table in tables:
        admin.add_view(CustomView(table, db.session))

class ProductView(CustomView):

    column_searchable_list = ('name',)
    column_filters = ('name', 'cost', 'product_type')

