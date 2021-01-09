from flask import Blueprint, render_template
from __main__ import *

settings_blueprint = Blueprint('settings', __name__)

@settings_blueprint.route('/settings')
def settings():
    context = {
        'is_settings': True,
        'premium': premium
    }
    return render_template('settings.html', **context)