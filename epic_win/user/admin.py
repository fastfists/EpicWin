from .models import Users, Role
from epic_win.ext import admin, db
from flask_admin.contrib.sqla import ModelView

def init_admin():
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Role, db.session))
