from flask import Blueprint, render_template, abort

goals_blueprint = Blueprint('goals', __name__, template_folder='templates', url_prefix='/hello1')


@goals_blueprint.route('/')
def hello_world():
    return 'Hello!!!! Werld!'
