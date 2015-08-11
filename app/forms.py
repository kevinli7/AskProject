from flask.ext.wtf import Form, RecaptchaField
from wtforms import StringField, BooleanField, TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Required, Length

from .models import User

class LoginForm(Form):
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [Required()])
    remember_me = BooleanField('remember_me', default=False)

class RegisterForm(Form):
    name = TextField('Username', [Required()])
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message='Passwords must match')
        ])
    # accept_tos = BooleanField('I accept the TOS', [Required()])
    # recaptcha = RecaptchaField()

    def validate(self):
        if not Form.validate(self):
            return False
        error = False
        if User.query.filter_by(email=self.email.data).first():
            self.email.errors.append("An account with that email is already registered.")
            error = True
        if User.query.filter_by(name=self.name.data).first():
            self.name.errors.append("That username is taken.")
            error = True
        return not error

class EditForm(Form):
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])