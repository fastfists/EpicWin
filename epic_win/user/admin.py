from .models import Users, Role
from epic_win.ext import admin, db
from epic_win.admin import CustomView

def init_admin():
    admin.add_view(UserAdmin(Users, db.session))
    admin.add_view(CustomView(Role, db.session))

class UserAdmin(CustomView):
    column_searchable_list = ('username',)
    column_filters = ('username', 'email')