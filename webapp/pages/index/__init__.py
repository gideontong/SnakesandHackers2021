from flask import Blueprint, render_template
from __main__ import *

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    global premium
    context = {
        'is_index': True,
        'commands': '32,567,841',
        'sales': '$15,340',
        'tickets': 42,
        'online': '4,311',
        'premium': premium
    }
    return render_template('index.html', **context)