from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
def index():
    item = {"name": "Nike Air Hurricanes",
            "price": 60,
            "image_url": "/static/images/item.png"
            }
    return render_template("public/index.html", items=[item for i in range(5)])

@public.route('/about')
def about():
    return render_template("public/about.html")

