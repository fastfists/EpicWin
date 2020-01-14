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
    product_type = db.Column(db.Text, nullable=False)
    image_name = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, unique=True)
    slug = db.Column(db.Text, index=True, unique=True)
    cost = db.Column(db.DECIMAL, nullable=False)
    description_long = db.Column(db.Text, nullable=True)
    description_short = db.Column(db.Text, nullable=True)

    # List of all sizes???
    def __repr__(self):
        return f"<Product {self.name} - ${self.cost}> "

    def __repr__(self):
        return f"{self.name} - ${self.cost}"

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
    is_checkout = db.Column(db.Boolean(), default=False)

    user = db.relationship("Users", backref="purchases")

    def __repr__(self):
        return f"<Purchase ({self.id}) - Total: {self.calc_total()}>"

    def __str__(self):
        return f"({self.id}) - Total: {self.calc_total()}"

    def calc_total(self):
        return sum([ item.calc_total() for item in self.items])


class PurchaseItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    count = db.Column(db.Integer, nullable=False, default=1)

    product = db.relationship("Product", backref="purchase_items")
    def __repr__(self):
        return f"<PurchaseItem ({self.product.name}) * {self.count} - Total: {self.calc_total()}>"

    def __repr__(self):
        return f"({self.product.name}) * {self.count} - Total: {self.calc_total()}"
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

