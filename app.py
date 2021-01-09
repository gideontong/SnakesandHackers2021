from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
premium = True

@app.route('/')
def index():
    # commands, earnings, tickets
    context = {
        'is_index': True,
        'premium': premium
    }
    return render_template('index.html', **context)