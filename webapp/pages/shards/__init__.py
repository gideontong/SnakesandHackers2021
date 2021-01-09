from flask import Blueprint, render_template
from __main__ import *

shards_blueprint = Blueprint('shards', __name__)

@app.route('/shards')
def shards():
    context = {
        'is_shards': True,
        'premium': premium
    }
    return render_template('shards.html', **context)