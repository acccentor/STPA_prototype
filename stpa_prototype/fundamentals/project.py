from flask import Blueprint, render_template, request, url_for, redirect
from stpa_prototype.database import db_session
from stpa_prototype.models import Project
from flask_security.decorators import login_required
from flask_security.core import current_user

project_blueprint = Blueprint('project', __name__, template_folder='templates', url_prefix='/project')


@project_blueprint.route('/')
@login_required
def index():
    print current_user.id
    print current_user.projects
    return render_template('fundamentals/project/index.html',
                           projects=current_user.projects
                           )

#
# @project_blueprint.route('/new', methods=['GET', 'POST'])
# @login_required
# def new():
#     if request.method == 'POST':
#         goals = Project(request.form['title'], request.form['text'])
#         db_session.add(goals)
#         db_session.commit()
#         return redirect(url_for('goals.index'))
#     return render_template('fundamentals/goals/new.html')
#
#
# @project_blueprint.route('/<goal_id>', methods=['GET', 'POST'])
# @login_required
# def show_or_update(goal_id):
#     goal_item = Goal.query.get(goal_id)
#     if request.method == 'GET':
#         return render_template('fundamentals/goals/view.html', goal=goal_item)
#     goal_item.title = request.form['title']
#     goal_item.text = request.form['text']
#     goal_item.vcs_check = ('vcs_check.%d' % goal_id) in request.form
#     db_session.commit()
#     return redirect(url_for('goals.index'))
