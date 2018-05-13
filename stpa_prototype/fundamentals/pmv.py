from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from stpa_prototype.database.project_models import PMV
from flask_security.decorators import login_required

from stpa_prototype.wtforms.forms import PMVForm

pmv_blueprint = Blueprint('pmv', __name__, template_folder='templates', url_prefix='/pmv')


# TODO remove test functions
@pmv_blueprint.route('/hello')
def hello_world():
    return 'Hello!!!! Werld!'


@pmv_blueprint.route('/test')
def test():
    print session['active_project_db']
    db = ProjectDB(session['active_project_db']).get_project_db_session()
    db.add(PMV('thisistest', 'still test'))
    db.query(PMV).all()
    db.close()
    return 'Hello!!!! Werld!'


@pmv_blueprint.route('/')
@login_required
def index():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
    project_db_session.close()
    return render_template('fundamentals/pmv/index.html',
                           pmv=pmv_list
                           )


@pmv_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PMVForm(request.form)
    if request.method == 'POST' and form.validate():
        project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
        pmv = PMV(form.title.data, form.text.data)
        project_db_session.add(pmv)
        project_db_session.commit()
        project_db_session.close()
        return redirect(url_for('pmv.index'))
    return render_template('fundamentals/pmv/new.html', form=form)


@pmv_blueprint.route('/<pmv_id>', methods=['GET', 'POST'])
@login_required
def show_or_update(pmv_id):
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    pmv_item = project_db_session.query(PMV).get(pmv_id)
    if request.method == 'POST':
        form = PMVForm(request.form)
        if form.validate():
            form.populate_obj(pmv_item)
            # pmv_item.title = request.form['title']
            # pmv_item.text = request.form['text']
            # pmv_item.vcs_check = ('vcs_check.%d' % pmv_id) in request.form
            project_db_session.commit()
            project_db_session.close()
            return redirect(url_for('pmv.index'))
    form = PMVForm(obj=pmv_item)
    project_db_session.close()
    return render_template('fundamentals/pmv/view.html', form=form)
