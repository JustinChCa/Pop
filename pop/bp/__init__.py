import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

bp = Blueprint('bp', __name__)


@bp.route('/')
@bp.route('/index')
@bp.route('/home')
def index():
    return render_template('index.html', title='Home')
