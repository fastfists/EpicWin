from .views import views
from .models import *
from .admin import init_admin

def init_app(app):
    app.register_blueprint(views)
    init_admin()

