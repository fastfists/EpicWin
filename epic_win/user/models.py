from epic_win.ext import db, login_manager
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"<Role: {self.name}>"

    def __str__(self):
        return f"{self.name}"

class Users(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='dynamic'))
    profile_picture = db.Column(db.String(20))
    
    
    def __repr__(self):
        return f"<User: {self.username} - {self.email}>"

    def __str__(self):
        return f"{self.username} - {self.email}"

    def get_cart(self):
        for purchase in self.purchases:
            if purchase.is_checkout == True:
                return purchase
        return None
    
