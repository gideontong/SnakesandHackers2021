from flask import Blueprint, render_template
from __main__ import *

notifications_blueprint = Blueprint('notifications', __name__)

@notifications_blueprint.route('/notifications')
def alerts():
    context = {
        'premium': premium
    }
    return render_template('notifications.html', **context)