from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    # commands, earnings, tickets
    return render_template('index.html')