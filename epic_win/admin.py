from flask_admin import AdminIndexView

class IndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
