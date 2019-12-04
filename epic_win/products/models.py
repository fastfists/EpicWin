from epic_win.ext import db, login_manager
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prodcut_type = db.Column(db.String(3), nullable=False)
    image_name = db.Column(db.String(25), nullable=False)
    slug = db.Column(db.String(50), index=True)
    name = db.Column(db.String(50), unique=True)
    cost = db.Column(db.String(20), nullable=False)
    description_long = db.Column(db.Text())
    description_short = db.Column(db.String(100))

    def get_cost(self):
        return self.cost

class Purchase(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    purchase_date = db.Column(db.DateTime(), default=datetime.utcnow)
    items = db.relationship("PurchaseItem", backref="purchase")

    def calc_total(self):
        return sum([ item.calc_total() for item in self.items])



class PurchaseItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    count = db.Column(db.Integer, nullable=False, default=1)

    def calc_total(self):
        return self.product.get_cost() * self.count

"""
    https://app.quickdatabasediagrams.com/#/d/Kv2fMX
    Coupons type:
        Percentage Discount (PER): (20% off) discount = 0.2
        Money off (SUB): ($20 off )discount = 20.00

    Missing:
        Order size
        Order colors
"""
