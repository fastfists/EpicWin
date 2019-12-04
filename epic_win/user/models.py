from epic_win.ext import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    profile_picture = db.Column(db.String(20))
    password = db.Column(db.String(40))


