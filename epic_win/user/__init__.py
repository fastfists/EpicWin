from .models import Users
from .admin import init_admin
from .views import user

def init_app(app):
    app.register_blueprint(user)
    init_admin()
