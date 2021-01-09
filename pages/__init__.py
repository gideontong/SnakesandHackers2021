from flask import Blueprint, render_template

index = Blueprint('index', __name__)

index.route('/')
def index():
    context = {
        'is_index': True,
        'premium': True
    }
    return render_template('index.html', **context)