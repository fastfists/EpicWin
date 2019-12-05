from .models import Users
from epic_win.ext import ma

class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users
        exclude = ["id"]

