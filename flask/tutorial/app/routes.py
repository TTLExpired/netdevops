from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bill'}
    posts = [
        {
            'author': {'username': 'Bill'},
            'body': 'This is my first blog'
        },
        {
            'author': {'username': 'Benji'},
            'body': 'I love Fornight'
        }
    ]
    return render_template('index.html', user=user, post=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)