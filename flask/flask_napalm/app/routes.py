from flask import render_template, redirect, flash
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def indes():
    return 'Welcome to NAPALM! Comms Site'

@app.route('/form', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Validate all Data
    if form.validate_on_submit():
        flash('Wrong Data. Please re-submit')
        return redirect('/form')
    return render_template('form.html', form=form)