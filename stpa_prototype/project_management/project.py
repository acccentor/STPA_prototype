from flask import Blueprint, render_template, request, url_for, redirect
from stpa_prototype.database import db_session
from stpa_prototype.models import Project
from flask_security.decorators import login_required
from flask_security.core import current_user

project_blueprint = Blueprint('project', __name__, template_folder='templates', url_prefix='/project')


@project_blueprint.route('/')
@login_required
def index():
    return render_template('project_management/index.html',
                           projects=current_user.projects
                           )


@project_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        project = Project(request.form['title'], request.form['text'], current_user)
        db_session.add(project)
        db_session.commit()
        return redirect(url_for('project.index'))
    return render_template('project_management/new.html')
#
#
# @project_blueprint.route('/<project_id>', methods=['GET', 'POST'])
# @login_required
# def show_or_update(project_id):
#     project_item = project.query.get(project_id)
#     if request.method == 'GET':
#         return render_template('fundamentals/projects/view.html', project=project_item)
#     project_item.title = request.form['title']
#     project_item.text = request.form['text']
#     project_item.vcs_check = ('vcs_check.%d' % project_id) in request.form
#     db_session.commit()
#     return redirect(url_for('projects.index'))
