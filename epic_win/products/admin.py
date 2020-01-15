from .models import *
from epic_win.ext import admin, db
from epic_win.admin import CustomView

def init_admin():
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(PurchaseView(Purchase, db.session))
    admin.add_view(PurchaseView(PurchaseItem, db.session))

    tables = [Discount, OrderOption, Coupon, Reviews]
    for table in tables:
        admin.add_view(CustomView(table, db.session))

class ProductView(CustomView):

    column_searchable_list = ('name',)
    column_filters = ('name', 'cost', 'product_type')

class PurchaseView(CustomView):

    can_edit = False
    can_create = False
    can_delete = False

