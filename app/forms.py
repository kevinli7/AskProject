from flask.ext.wtf import Form, RecaptchaField
from wtforms import StringField, BooleanField, TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Required, Length

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

class EditForm(Form):
	about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])