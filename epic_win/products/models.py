from epic_win.ext import db, login_manager

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_slug = db.Column(db.String(50), index=True)
    name = db.Column(db.String(50), unique=True)
    cost = db.Column(db.String(20), nullable=False)
    image_name = db.Column(db.String(25), nullable=False)

class Orders(db.Model):
    pass


"""
    https://app.quickdatabasediagrams.com/#/d/Kv2fMX
    Coupons type:
        Percentage Discount (PER): (20% off) discount = 0.2
        Money off (SUB): ($20 off )discount = 20.00

    Missing:
        Order size
        Order colors
"""

