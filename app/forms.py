from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, DataRequired

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class UserAddForm(Form):
    host = TextField(default='hostname-admin.ukraine.ptec', validators = [DataRequired()])
    name = TextField(default='testuser')
    passwd = TextField(default='supersecretpass')
    email = TextField()
    firstname = TextField()
    middlename = TextField()
    lastname = TextField()
    notify = BooleanField(default=True)
    port = TextField()
    roles = TextField()
    orgroles = TextField()
    siteroles = TextField()
    orgs = TextField()
    locale = TextField()

