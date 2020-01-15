from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from epic_win.ext import security
from flask_security.forms import RegisterForm, StringField, Required, current_user

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [Required()])

class IndexView(AdminIndexView):

    def is_accessible(self):
        return is_admin()

class CustomView(ModelView):

    list_template = 'admin/list.html'
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    def is_accessible(self):
        return is_admin()

    def _handle_view(self, name, **kwargs):
        """
            Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

def is_admin():

    return (current_user.is_active and
            current_user.is_authenticated and
            current_user.has_role('Admin')
    )
