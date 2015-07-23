from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : "DOGE"}
    posts = [
        {
            'author': {'nickname': "DogeLuvr69"},
        'body': 'So many DOGES in the house!!'
    },
    {
        'author': {'nickname': 'Doge Enthusiast'},
        'body': 'WHO LET THE DOGES OUT'
    }
    ]
    return render_template('index.html',
                            title='DOGELAND', 
                user=user,
                posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for email="%s", remember_me=%s' %
              (form.email.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('New User: user="%s", email=%s' %
              (form.name.data, form.email.data))
        return redirect('/index')
    return render_template('register.html',
                            title='Register for DOGEWORLD',
                            form=form)
