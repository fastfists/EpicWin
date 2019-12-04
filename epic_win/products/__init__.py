from .views import views
from .models import *

def init_app(app):
    app.register_blueprint(views)

