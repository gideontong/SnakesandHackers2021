from flask import Blueprint, render_template
from __main__ import *

log_blueprint = Blueprint('log', __name__)

@log_blueprint.route('/log')
def log():
    context = {
        'premium': premium
    }
    return render_template('log.html', **context)