from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
import random

@app.route('/')
@app.route('/index')
def index():

    # Generate a fake greeting
    rand = random.uniform(0, 1)
    if rand > 0.5:
        user = {'username':'Albert'}
    else:
        user = {'username':'Fredje'}

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

    return render_template('index.html', user=user, cheese="Cheeseball", posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)

@app.route('/stront')
def stront():
    return "Hey stront"