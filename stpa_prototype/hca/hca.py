from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from flask_security.decorators import login_required

# from stpa_prototype.wtforms.forms import HCAForm
from stpa_prototype.database.project_models import ControlAction, PMV

hca_blueprint = Blueprint('hca', __name__, template_folder='templates', url_prefix='/hca')


# @hca_blueprint.route('/')
# @login_required
# def index():
    # project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    # hca_list = project_db_session.query(HCA).order_by(HCA.id.asc()).all()
    # project_db_session.close()
    # return render_template('fundamentals/hca/index.html',
    #                        hca=hca_list
    #                        )

#
# def genereate_context_table():
#     project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
#     ca_list = project_db_session.query(ControlAction).order_by(ControlAction.id.asc()).all()
#     pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
#     context_table = []
#     for ca in ca_list:
#