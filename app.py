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
    return render_template('statistics.html', **context)

@app.route('/settings')
def settings():
    context = {
        'is_settings': True,
        'premium': premium
    }
    return render_template('settings.html', **context)

@app.route('/shards')
def shards():
    context = {
        'is_shards': True,
        'premium': premium
    }
    return render_template('shards.html', **context)

@app.route('/guilds')
def guilds():
    context = {
        'is_guilds': True,
        'premium': premium
    }
    return render_template('guilds.html', **context)

@app.route('/channels')
def channels():
    context = {
        'is_channels': True,
        'premium': premium
    }
    return render_template('channels.html', **context)

@app.route('/users')
def users():
    context = {
        'is_users': True,
        'premium': premium
    }
    return render_template('users.html', **context)
