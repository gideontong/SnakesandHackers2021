from flask import Flask, render_template

app = Flask(__name__)
premium = True

from webapp import blueprints

for blueprint in blueprints:
    app.register_blueprint(blueprint)

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