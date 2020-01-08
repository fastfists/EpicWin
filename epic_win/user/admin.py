from .models import Users
from epic_win.ext import admin, db
from flask_admin.contrib.sqla import ModelView

def init_admin():
    admin.add_view(ModelView(Users, db.session))
