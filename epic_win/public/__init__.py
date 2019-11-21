from .views import public

def init_app(app):
    app.register_blueprint(public)
