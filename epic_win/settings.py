from os import getenv

FLASK_APP=getenv("FLASK_APP")
FLASK_DEBUG=1
FLASK_ADMIN_SWATCH="cerulean"
SQLALCHEMY_DATABASE_URI=getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY=getenv("SECRET_KEY")


# Flask-Security config
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end

SECURITY_POST_LOGIN_VIEW = "/shop"
SECURITY_POST_LOGOUT_VIEW = "/"
SECURITY_POST_REGISTER_VIEW = "/login"

# Flask-Security features

SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = False
SECURITY_RECOVERABLE = True

# Flask-Security Email features

EMAIL_SUBJECT_REGISTER = "Welcome to the Epic rewards program"
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'epic.wins.company@gmail.com'
MAIL_PASSWORD = 'Epic.win1'
