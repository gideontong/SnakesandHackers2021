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

@app.route('/statistics')
def statistics():
    pass

@app.route('/settings')
def settings():
    pass

@app.route('/shards')
def shards():
    pass

@app.route('/guilds')
def guilds():
    pass

@app.route('/channels')
def channels():
    pass

@app.route('/users')
def users():
    pass
