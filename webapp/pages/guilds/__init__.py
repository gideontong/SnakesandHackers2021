from flask import Blueprint, render_template
from __main__ import *

guilds_blueprint = Blueprint('guilds', __name__)

@guilds_blueprint.route('/guilds')
def guilds():
    context = {
        'is_guilds': True,
        'premium': premium
    }
    return render_template('guilds.html', **context)