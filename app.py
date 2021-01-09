from flask import Flask, render_template

app = Flask(__name__)
premium = True

from webapp.pages import index_blueprint

app.register_blueprint(index_blueprint)

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

@app.route('/notifications')
def alerts():
    context = {
        'premium': premium
    }
    return render_template('notifications.html', **context)

@app.route('/me')
def profile():
    context = {
        'premium': premium
    }
    return render_template('profile.html', **context)

@app.route('/log')
def log():
    context = {
        'premium': premium
    }
    return render_template('log.html', **context)

@app.route('/logout')
def logout():
    return render_template('logout.html')

app.run()