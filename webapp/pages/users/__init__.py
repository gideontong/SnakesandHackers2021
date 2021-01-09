from flask import Blueprint, render_template
from __main__ import *

users_blueprint = Blueprint('users', __name__)

@app.route('/users')
def users():
    context = {
        'is_users': True,
        'premium': premium
    }
    return render_template('users.html', **context)