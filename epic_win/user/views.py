from flask import Blueprint, render_template, request
from epic_win.ext import login_manager, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required
from .schemas import UserSchema


user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        schema = UserSchema()
        schmea.load(request.form)
        user = user.query.get(schema.get('name'))
        if user and bcrypt.check_password_hash(user.password, schema.password):
            next_page = request.args.get('next')
            flash("You are now logged in", "success")
            return redirect(next_page) if next_page else redirect(url_for('public.index'))
    return render_template('user/login.html')

@user.route('/logout')
def logout():

    logout_user()
    flash("You have been logged out", 'info')
    return redirect(url_for('public.index'))

@user.route('/account')
@login_required
def account():
    return render_template('user/account.html', user=current_user)    

