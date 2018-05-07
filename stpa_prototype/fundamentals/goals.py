from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from stpa_prototype.database.models import Goal
from flask_security.decorators import login_required

from stpa_prototype.wtforms.forms import GoalForm

goals_blueprint = Blueprint('goals', __name__, template_folder='templates', url_prefix='/goals')


# TODO remove test functions
@goals_blueprint.route('/hello')
def hello_world():
    return 'Hello!!!! Werld!'


@goals_blueprint.route('/test')
def test():
    print session['active_project_db']
    db = ProjectDB(session['active_project_db']).get_project_db_session()
    db.add(Goal('thisistest', 'still test'))
    db.query(Goal).all()
    db.close()
    return 'Hello!!!! Werld!'


@goals_blueprint.route('/')
@login_required
def index():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    goals_list = project_db_session.query(Goal).order_by(Goal.id.asc()).all()
    project_db_session.close()
    return render_template('fundamentals/goals/index.html',
                           goals=goals_list
                           )


@goals_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = GoalForm(request.form)
    if request.method == 'POST' and form.validate():
        project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
        goals = Goal(form.title.data, form.text.data)
        project_db_session.add(goals)
        project_db_session.commit()
        project_db_session.close()
        return redirect(url_for('goals.index'))
    return render_template('fundamentals/goals/new.html', form=form)


@goals_blueprint.route('/<goal_id>', methods=['GET', 'POST'])
@login_required
def show_or_update(goal_id):
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    goal_item = project_db_session.query(Goal).get(goal_id)
    if request.method == 'POST':
        form = GoalForm(request.form)
        if form.validate():
            form.populate_obj(goal_item)
            # goal_item.title = request.form['title']
            # goal_item.text = request.form['text']
            # goal_item.vcs_check = ('vcs_check.%d' % goal_id) in request.form
            project_db_session.commit()
            project_db_session.close()
            return redirect(url_for('goals.index'))
    form = GoalForm(obj=goal_item)
    project_db_session.close()
    return render_template('fundamentals/goals/view.html', form=form)
