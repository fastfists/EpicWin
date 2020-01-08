import autoapp
from slugify import slugify
from epic_win.ext import db
from epic_win.products.models import Product
import csv

db.drop_all()
db.create_all()

with open('products.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:

        product = Product(
                name=row.get("Display Name"),
                prodcut_type=row.get("Category"),
                image_name=f"{row.get('Image Name')}.png",
                slug=slugify(row.get("Display Name")),
                cost=row.get("Cost"),
                description_long=row.get("Long Description"),
                description_short=row.get("Short description")
                )
        print(Product)

        db.session.add(product)
        db.session.commit()
