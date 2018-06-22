from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_security.decorators import login_required

from stpa_prototype.project_management.vcs import get_repo, add_and_commit


vcs_blueprint = Blueprint('vcs', __name__, template_folder='templates', url_prefix='/vcs')


@vcs_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    project_id = session['active_project_db']
    repo = get_repo(project_id)
    if request.method == 'POST':
        add_and_commit(project_id)

    return render_template('project_management/vcs/index.html',
                           commits=list(repo.iter_commits())
                           )
