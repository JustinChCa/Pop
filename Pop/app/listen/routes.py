import functools
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

routes = Blueprint('routes', __name__)


@routes.route('/')
@routes.route('/index')
@routes.route('/home')
def index():
    if 'username' not in session:
        return redirect(url_for('routes.login'))

    return render_template('index.html')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('routes.index'))

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('routes.index'))

    return render_template('login.html')


@routes.route('/logout')
def logout():
    if 'username' in session:
        del session['username']

    return redirect(url_for('routes.login'))
