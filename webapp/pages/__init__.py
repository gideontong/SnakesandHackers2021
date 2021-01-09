from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    context = {
        'is_index': True,
        'premium': True
    }
    return render_template('index.html', **context)