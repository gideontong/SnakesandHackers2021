from flask import Blueprint, render_template
from __main__ import *

channels_blueprint = Blueprint('channels', __name__)

@app.route('/channels')
def channels():
    context = {
        'is_channels': True,
        'premium': premium
    }
    return render_template('channels.html', **context)