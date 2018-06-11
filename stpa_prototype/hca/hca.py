from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from flask_security.decorators import login_required

# from stpa_prototype.wtforms.forms import HCAForm
from stpa_prototype.database.project_models import ControlAction, PMV, HCA
from stpa_prototype.wtforms.forms import HCAAddHazard, CAHazard

hca_blueprint = Blueprint('hca', __name__, template_folder='templates', url_prefix='/hca')


# @hca_blueprint.route('/')
# @login_required
# def index():
#     project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
#     pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
#     ca_list = project_db_session.query(ControlAction).order_by(ControlAction.id.asc()).all()
#     cross_pmvv_list = recursive(pmv_list, [], [])
#     hca_entries = []
#     for ca in ca_list:
#         for cross_pmvv in cross_pmvv_list:
#             # hca = HCA(ca, cross_pmvv)
#             hca = HCA(ca)
#             for pmvv in cross_pmvv:
#                 hca.pmvvs.append(pmvv)
#             hca_entries.append(hca)
#     print hca_entries
#
#     return 'test'


@hca_blueprint.route('/')
@login_required
def index():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    hca_list = project_db_session.query(HCA).order_by(HCA.id.asc()).all()
    return render_template('hca/index.html', hca_list=hca_list)
    # TODO db session close after return, so never run, this method will look db for vcs
    # project_db_session.close()


@hca_blueprint.route('/test')
@login_required
def test():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    hca_list = project_db_session.query(HCA).order_by(HCA.id.asc()).all()
    hca_hazard_button_form = CAHazard()
    for hca in hca_list:
        hca_hazard_button = HCAAddHazard()
        hca_hazard_button.id = hca.id
        hca_hazard_button_form.hazards.append_entry(hca_hazard_button)
    return render_template('hca/index.html', hca_list=hca_list, add_hazard_form=hca_hazard_button_form)
    # TODO db session close after return, so never run, this method will look db for vcs
    # project_db_session.close()


@hca_blueprint.route('/write')
@login_required
def write():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
    ca_list = project_db_session.query(ControlAction).order_by(ControlAction.id.asc()).all()
    cross_pmvv_list = recursive(pmv_list, [], [])
    hca_entries = []
    for ca in ca_list:
        for cross_pmvv in cross_pmvv_list:
            # hca = HCA(ca, cross_pmvv)
            hca = HCA(ca)
            for pmvv in cross_pmvv:
                hca.pmvvs.append(pmvv)
            hca_entries.append(hca)
    # print hca_entries
    for hca in hca_entries:
        project_db_session.add(hca)
    project_db_session.commit()
    project_db_session.close()

    return 'test'


def recursive(remaining_columns, path, result):
    # print 'recursive'
    if not remaining_columns:
        # print 'not remaining_colums'
        return path
    for payload in remaining_columns[0].pmvvs:
        # print 'path: ' + format(path)
        # print 'payload: ' + format(payload)
        # print 'result b: ' + format(result)
        # print 'remaining: ' + format(remaining_columns)
        # print 'remainging[1:]' + format(remaining_columns[1:])
        if not remaining_columns[1:]:
            result.append(recursive(remaining_columns[1:], path + [payload], result))
        else:
            recursive(remaining_columns[1:], path + [payload], result)
    return result
#
#
# class testclass():
#     list = []
#
# def product(pmv_list):
#     hca_table = []
#     # pmvv_talbe = [[]]
#     y = 0
#     # for i in range(1, len(pmv_list)):
#     #     hca_table.
#
#     for pmv in pmv_list:
#         x = 0
#         for pmvv in pmv.pmvvs:
#             print format(pmv.id) + ', ' + format(pmvv.id)
#             x += 1
#         y += 1

# def genereate_context_table():
#     project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
#     ca_list = project_db_session.query(ControlAction).order_by(ControlAction.id.asc()).all()
#     pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
#     context_table = []
#     for ca in ca_list:
#