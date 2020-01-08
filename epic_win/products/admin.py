from .models import *
from epic_win.ext import admin, db
from flask_admin.contrib.sqla import ModelView

def init_admin():
    tables = [Product, Discount, Purchase, PurchaseItem, OrderOption, Coupon, Reviews]
    for table in tables:
        admin.add_view(ModelView(table, db.session))
