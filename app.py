from flask import Flask, render_template

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
    context = {
        'is_stats': True,
        'premium': premium
    }
    pass

@app.route('/settings')
def settings():
    context = {
        'is_settings': True,
        'premium': premium
    }
    pass

@app.route('/shards')
def shards():
    context = {
        'is_shards': True,
        'premium': premium
    }
    pass

@app.route('/guilds')
def guilds():
    context = {
        'is_guilds': True,
        'premium': premium
    }
    pass

@app.route('/channels')
def channels():
    context = {
        'is_channels': True,
        'premium': premium
    }
    pass

@app.route('/users')
def users():
    pass
