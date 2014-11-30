from flask_wtf import Form
from wtforms import TextField, PasswordField
#from wtforms import validators
from wtforms.validators import Required


class domain_submit(Form):
    domain = TextField('domain', validators=[Required()])
