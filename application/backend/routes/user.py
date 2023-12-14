from flask import Blueprint, render_template

home_bp = Blueprint('user', __name__)


@home_bp.route('/', methods=['GET'])
def home_page():
    return render_template("index2.html")


def init_app(app):
    app.register_blueprint(home_bp)
