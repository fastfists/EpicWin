from flask import Flask


def create_app(config_object='epic_win.settings') -> Flask:
    from . import user
    from . import public

    app = Flask(__name__)
    app.config.from_object(config_object)

    user.init_app(app)
    public.init_app(app)

    register_extensions(app)

    return app

def register_extensions(app):
    from epic_win.ext import migrate, ma, admin, db, sekazi, login_manager, bcrypt

    admin.init_app(app)
    db.init_app(app)
    db.app = app

    login_manager.init_app(app)
    sekazi.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

