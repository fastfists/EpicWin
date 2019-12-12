from epic_win.ext import db, login_manager
from datetime import datetime

"""
    https://app.quickdatabasediagrams.com/#/d/Kv2fMX
    Coupons type:
        Percentage Discount (PER): (20% off) discount = 0.2
        Money off (SUB): ($20 off )discount = 20.00
    Missing:
        Order size
        Order colors
"""

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    prodcut_type = db.Column(db.String(3), nullable=False)
    image_name = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(50), unique=True)
    slug = db.Column(db.String(50), index=True)
    cost = db.Column(db.DECIMAL, nullable=False)
    description_long = db.Column(db.Text())
    description_short = db.Column(db.String(100))

    # List of all sizes???

    def get_cost(self):
        return self.cost

product_discounts = db.Table('product_discounts',
        db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
        db.Column('discount_id', db.Integer, db.ForeignKey('discount.id')))


class Discount(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    discount_type = db.Column(db.String(3))
    discount = db.Column(db.DECIMAL, nullable=False)
    experiation_date = db.Column(db.DateTime, nullable=False)

    products = db.relationship('Product', secondary=product_discounts, backref='discount')


class Purchase(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    purchase_date = db.Column(db.DateTime(), default=datetime.utcnow)
    payment_confrimation = db.Column(db.String(20))

    items = db.relationship("PurchaseItem", backref="purchase")

    def calc_total(self):
        return sum([ item.calc_total() for item in self.items])


class PurchaseItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    count = db.Column(db.Integer, nullable=False, default=1)
    # color
    # size

    def calc_total(self):
        return self.product.get_cost() * self.count


class OrderOption(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    shipping_type = db.Column(db.String)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'))

    coupon = db.relationship("Coupon", backref="order_options")


user_coupons = db.Table('user_coupons',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('coupon_id', db.Integer, db.ForeignKey('coupon.id')))


class Coupon(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    discount_type = db.Column(db.String(3))
    discount = db.Column(db.DECIMAL, nullable=False)
    experiation_date = db.Column(db.DateTime, nullable=False)

    users = db.relationship('Users', secondary=user_coupons, backref='coupon')


class Reviews(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    star_rating = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

