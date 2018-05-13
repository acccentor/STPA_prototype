from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from stpa_prototype.database.project_models import ControlAction
from flask_security.decorators import login_required

from stpa_prototype.wtforms.forms import ControlActionForm

ca_blueprint = Blueprint('ca', __name__, template_folder='templates', url_prefix='/ca')


@ca_blueprint.route('/')
@login_required
def index():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    ca_list = project_db_session.query(ControlAction).order_by(ControlAction.id.asc()).all()
    project_db_session.close()
    return render_template('fundamentals/ca/index.html',
                           ca=ca_list
                           )


@ca_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = ControlActionForm(request.form)
    if request.method == 'POST' and form.validate():
        project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
        ca = ControlAction(form.title.data, form.text.data)
        project_db_session.add(ca)
        project_db_session.commit()
        project_db_session.close()
        return redirect(url_for('ca.index'))
    return render_template('fundamentals/ca/new.html', form=form)


@ca_blueprint.route('/<ca_id>', methods=['GET', 'POST'])
@login_required
def show_or_update(ca_id):
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    ca_item = project_db_session.query(ControlAction).get(ca_id)
    if request.method == 'POST':
        form = ControlActionForm(request.form)
        if form.validate():
            form.populate_obj(ca_item)
            # ca_item.title = request.form['title']
            # ca_item.text = request.form['text']
            # ca_item.vcs_check = ('vcs_check.%d' % ca_id) in request.form
            project_db_session.commit()
            project_db_session.close()
            return redirect(url_for('ca.index'))
    form = ControlActionForm(obj=ca_item)
    project_db_session.close()
    return render_template('fundamentals/ca/view.html', form=form)
