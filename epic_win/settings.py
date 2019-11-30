from os import getenv


FLASK_APP=getenv("autoapp")
FLASK_DEBUG=getenv("1")
FLASK_ENV=getenv("development")
FLASK_ADMIN_SWATCH=getenv("cerulean")
SQLALCHEMY_TRACK_MODIFICATIONS=getenv("False")
