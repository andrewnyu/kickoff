from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template(url_for('login'),title='Sign In', form=form)
