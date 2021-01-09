from flask import Blueprint, render_template
from __main__ import *

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    global premium
    context = {
        'is_index': True,
        'premium': premium
    }
    return render_template('index.html', **context)