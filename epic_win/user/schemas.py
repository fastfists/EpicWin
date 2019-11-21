from .models import User
from epic_win.ext import ma

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        exclude = ["id"]

