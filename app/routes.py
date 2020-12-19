from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():

    # # Generate a fake greeting
    # rand = random.uniform(0, 1)
    # if rand > 0.5:
    #     user = {'username':'Albert'}
    # else:
    #     user = {'username':'Fredje'}

    # Generate fake posts
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body': 'I like cheese'
        }
    ]

    return render_template('index.html', cheese="Cheeseball", posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next') # Did we get redirected to login from restricted page?
        if not next_page or url_parse(next_page).netloc != '': # Ensures redirect within same site
            next_page = url_for('index')
        return redirect(next_page) # Redirects either to index or original 'restricted' page
    return render_template("login.html", title="Sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/stront')
def stront():
    return "Hey stront"