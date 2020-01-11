from flask_admin import AdminIndexView
from flask_security.forms import RegisterForm, StringField, Required

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [Required()])

class IndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
