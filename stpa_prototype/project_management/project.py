import os

from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_security.core import current_user
from flask_security.decorators import login_required
import shutil

from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from stpa_prototype.database.models import Project
from stpa_prototype.project_management.vcs import init_db_repo, create_and_commit_master
from stpa_prototype.wtforms.forms import ProjectSelect

project_blueprint = Blueprint('project', __name__, template_folder='templates', url_prefix='/project')

os_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/db/projects"))

@project_blueprint.route('/')
@login_required
def index():
    current_project = session['active_project_db']
    return render_template('project_management/index.html',
                           projects=current_user.projects, current_project=int(current_project)
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
        form = ProjectSelect(request.form)
        if form.set_active.data:
            session['active_project_db'] = project_id
        elif form.delete.data:
            project = db_session.query(Project).get(project_id)
            db_session.delete(project)
            db_session.commit()
            path = "{}/{}".format(os_path, project_id)
            shutil.rmtree(path, ignore_errors=True)

    if request.method == 'GET':
        form = ProjectSelect()
        return render_template('project_management/view.html', form=form)
    return redirect(url_for('project.index'))
