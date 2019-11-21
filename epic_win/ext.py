from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sekazi import Sekazi

sekazi = Sekazi()
login_manager = LoginManager()
migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()
admin = Admin(template_mode="bootstrap3")
bcrypt = Bcrypt()

