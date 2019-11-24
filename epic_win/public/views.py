from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
def index():
    return render_template("public/index.html")

@public.route('/about')
def about():
    return render_template("public/about.html")

