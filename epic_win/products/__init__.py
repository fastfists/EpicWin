from .views import product

def init_app(app):
    app.register_blueprint(product)

