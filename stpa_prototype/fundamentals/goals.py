from flask import Blueprint, render_template, request, url_for, redirect
# from flask import current_app as app
# from stpa_prototype import Todo
from stpa_prototype.database import db_session
from stpa_prototype.models import Goals
goals_blueprint = Blueprint('goals', __name__, template_folder='templates', url_prefix='/goals')


@goals_blueprint.route('/hello')
def hello_world():
    return 'Hello!!!! Werld!'


@goals_blueprint.route('/')
def index():
    return render_template('fundamentals/goals/index.html',
                           goals=Goals.query.order_by(Goals.id.asc()).all()
                           )


@goals_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        goals = Goals(request.form['title'], request.form['text'])
        db_session.add(goals)
        db_session.commit()
        return redirect(url_for('goals.index'))
    return render_template('fundamentals/goals/new.html')


@goals_blueprint.route('/<int:todo_id>', methods=['GET', 'POST'])
def show_or_update(todo_id):
    goal_item = Goals.query.get(todo_id)
    if request.method == 'GET':
        return render_template('fundamentals/goals/view.html', todo=goal_item)
    goal_item.title = request.form['title']
    goal_item.text = request.form['text']
    goal_item.vcs_check = ('vcs_check.%d' % todo_id) in request.form
    db_session.commit()
    return redirect(url_for('goals.index'))
