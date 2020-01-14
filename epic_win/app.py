from flask import Flask
import paypalrestsdk as paypal
from flask_security import SQLAlchemyUserDatastore


def create_app(config_object='epic_win.settings') -> Flask:
    from . import user
    from . import public
    from . import products

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    init_security(app)

    user.init_app(app)
    public.init_app(app)
    products.init_app(app)

    print(app.config[ "PAYPAL_CLIENT_ID" ])
    paypal.configure({
        "mode": "sandbox",
        "client_id": app.config[ "PAYPAL_CLIENT_ID" ],
        "client_secret": app.config[ "PAYPAL_CLIENT_SECRET" ]})

    return app

def register_extensions(app):
    from epic_win.ext import migrate, ma, admin, db, login_manager, bcrypt, sekazi, security, mail

    admin.init_app(app)
    db.init_app(app)
    db.app = app

    sekazi.init_app(app)
    login_manager.init_app(app)
    sekazi.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)

def init_security(app):
    from epic_win.ext import security, db
    from epic_win.admin import ExtendedRegisterForm
    from .user import Users, Role

    print("initing")
    user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
    security.init_app(app, user_datastore,
            register_form=ExtendedRegisterForm)
