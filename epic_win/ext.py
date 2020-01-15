from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sekazi import Sekazi
from flask_security import Security
from flask_mail import Mail

sekazi = Sekazi()
login_manager = LoginManager()
migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
security = Security()
mail = Mail()

from epic_win.admin import IndexView

admin = Admin(index_view=IndexView() ,template_mode="bootstrap3", base_template="admin_template.html")