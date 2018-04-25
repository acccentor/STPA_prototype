from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_security.core import current_user
from flask_security.decorators import login_required

from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from stpa_prototype.database.models import Project
from stpa_prototype.project_management.vcs import init_db_repo, create_and_commit_master

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
        project_db = ProjectDB(project.id)
        session['active_project_db'] = project_db.project_id
        init_db_repo(project.id)
        project_db.init_db()
        create_and_commit_master(project.id)
        return redirect(url_for('project.index'))
    return render_template('project_management/new.html')


@project_blueprint.route('/<project_id>', methods=['GET', 'POST'])
@login_required
def show_or_update(project_id):
    if request.method == 'POST':
        session['active_project_db'] = project_id

    if request.method == 'GET':
        return render_template('project_management/view.html')

    return redirect(url_for('project.index'))
