from flask import Blueprint, render_template
from __main__ import *

statistics_blueprint = Blueprint('statistics', __name__)

@app.route('/statistics')
def statistics():
    context = {
        'is_stats': True,
        'premium': premium
    }
    return render_template('statistics.html', **context)