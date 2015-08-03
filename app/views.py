from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user,current_user, login_required
from app import app, db, lm
from .models import User
from .forms import LoginForm, RegisterForm
from werkzeug import check_password_hash, generate_password_hash


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
    #     {
    #         'author': {'nickname': "DogeLuvr69"},
    #     'body': 'So many DOGES in the house!!'
    # },
    # {
    #     'author': {'nickname': 'Doge Enthusiast'},
    #     'body': 'WHO LET THE DOGES OUT'
    # }
    ]
    return render_template('index.html', 
                title='DOGELAND',
                user=user,
                posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #Checks if a user is logged in already
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            session['remember_me'] = form.remember_me.data
            return redirect(request.args.get('next') or url_for('index'))
        flash('Wrong email or password', 'error-message')
    return render_template('login.html',
                            title='Sign In',
                            form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, 
            password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html',
                            title='Register for DOGEWORLD',
                            form=form)


""" HELPER FUNCTIONS """
@lm.user_loader
def load_user(id):
   return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
