from wtforms import Form, StringField, validators
from config import admin_secret_key
class Register(Form):
    username = StringField("username", [validators.Length(min=5,max=50)])
    password = StringField("password", [validators.Length(min=8)])
    repeat_password = StringField("repeat_password", [validators.Length(min=8), validators.EqualTo('password', message='Passwords must match')])
    job= StringField("job", [validators.AnyOf(['buyer','seller',"admin"])])
    email = StringField("email", [validators.Optional()])
    phone = StringField("phone", [validators.Optional()])
    address= StringField("address", [validators.Optional()])
    special_password = StringField("special_password", [validators.Optional(), validators.AnyOf([admin_secret_key])])
