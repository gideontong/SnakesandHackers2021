from flask import Blueprint, render_template

logout_blueprint = Blueprint('logout', __name__)

@logout_blueprint.route('/logout')
def logout():
    return render_template('logout.html')