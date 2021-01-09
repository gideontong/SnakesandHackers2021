from flask import Blueprint, render_template
from __main__ import *

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/me')
def profile():
    context = {
        'premium': premium
    }
    return render_template('profile.html', **context)