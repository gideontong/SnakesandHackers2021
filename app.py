from flask import Flask, render_template

app = Flask(__name__)
premium = True

from webapp import blueprints

for blueprint in blueprints:
    app.register_blueprint(blueprint)

app.run()