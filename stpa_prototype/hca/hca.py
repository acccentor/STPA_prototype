from flask import Blueprint, render_template, request, url_for, redirect, session
# from flask import current_app as app
# from stpa_prototype.database.database import db_session
from stpa_prototype.database.database_project import ProjectDB
from flask_security.decorators import login_required
# from stpa_prototype.wtforms.forms import HCAForm
from stpa_prototype.database.project_models import ControlAction, PMV, HCA, Hazard
from stpa_prototype.wtforms.forms import HCAAddHazard, CAHazard, HCACurrentHazards

hca_blueprint = Blueprint('hca', __name__, template_folder='templates', url_prefix='/hca')


def set_disabled(hca_id):
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    hca = project_db_session.query(HCA).get(hca_id)
    hca.hidden = not hca.hidden
    project_db_session.commit()
    project_db_session.close()


@hca_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    show_hide = False
    if request.method == 'POST':
        form = CAHazard(request.form)
        if form.show_hide.data:
            show_hide = True
        elif form.clear_table.data:
            write()
        else:
            for hazard in form.hazards:
                if hazard.add_cah.data:
                    return show_add_remove_hazard(hazard.hca_id.data, 0)
                elif hazard.add_cahtl.data:
                    return show_add_remove_hazard(hazard.hca_id.data, 1)
                elif hazard.add_cahte.data:
                    return show_add_remove_hazard(hazard.hca_id.data, 2)
                elif hazard.add_cahnp.data:
                    return show_add_remove_hazard(hazard.hca_id.data, 3)
                elif hazard.remove_hca.data:
                    set_disabled(hazard.hca_id.data)
            return redirect(url_for('hca.index'))
    hca_list = project_db_session.query(HCA).order_by(HCA.id.asc()).all()
    hca_hazard_button_form = CAHazard()
    for hca in hca_list:
        # TODO size instead of list
        # hazard_buttons = HCAAddHazard()
        hca_hazard_button_form.hazards.append_entry()
    for_loop_tuple = zip(hca_list, hca_hazard_button_form.hazards)
    for hca, hazard in for_loop_tuple:
        hazard.hca_id.data = hca.id
    return render_template('hca/index.html', for_loop_tuple=for_loop_tuple, hca_list=hca_list, show_hide=show_hide,
                           form=hca_hazard_button_form)
    # TODO db session close after return, so never run, this method will look db for vcs
    # project_db_session.close()


@hca_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_remove():
    if request.method == 'POST':
        form = HCACurrentHazards(request.form)
        project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
        hca = project_db_session.query(HCA).get(form.hca_id.data)
        cah_type = format(form.cah_type.data)
        current_hazards = None
        if cah_type == "0":
            current_hazards = hca.cah
        elif cah_type == "1":
            current_hazards = hca.cah_tl
        elif cah_type == "2":
            current_hazards = hca.cah_te
        elif cah_type == "3":
            current_hazards = hca.cah_np

        for hazard_button in form.possible_hazards:
            if hazard_button.add_button.data:
                hazard = project_db_session.query(Hazard).get(hazard_button.hazard_id.data)
                current_hazards.append(hazard)
                project_db_session.commit()
                return show_add_remove_hazard(form.hca_id.data, form.cah_type.data)
        for hazard_button in form.current_hazards:
            if hazard_button.remove_button.data:
                hazard = project_db_session.query(Hazard).get(hazard_button.hazard_id.data)
                current_hazards.remove(hazard)
                project_db_session.commit()
                return show_add_remove_hazard(cah_type, form.cah_type.data)
    return redirect(url_for('hca.index'))


def show_add_remove_hazard(hca_id, cah_type_raw):
    cah_type = format(cah_type_raw)
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    hca = project_db_session.query(HCA).get(hca_id)
    current_hazards = []
    if cah_type == "0":
        current_hazards = hca.cah
    elif cah_type == "1":
        current_hazards = hca.cah_tl
    elif cah_type == "2":
        current_hazards = hca.cah_te
    elif cah_type == "3":
        current_hazards = hca.cah_np

    all_hazards = project_db_session.query(Hazard).order_by(Hazard.id.asc()).all()
    possible_hazards = []
    for hazard_to_add in all_hazards:
        to_add = True
        for hazard_to_compare in current_hazards:
            # print "hazard to add: {}, hazard_to_compare: {}".format(hazard_to_add.id, hazard_to_compare.id)
            if hazard_to_add.id == hazard_to_compare.id:
                to_add = False
        if to_add:
            possible_hazards.append(hazard_to_add)

    add_remove_hazard_button = HCACurrentHazards()
    add_remove_hazard_button.hca_id.data = hca_id
    add_remove_hazard_button.cah_type.data = cah_type
    for hazard in current_hazards:
        add_remove_hazard_button.current_hazards.append_entry()
    current_hazards_tuple = zip(current_hazards, add_remove_hazard_button.current_hazards)
    for current_hazard, hazard_button in current_hazards_tuple:
        hazard_button.hazard_id.data = current_hazard.id

    for hazard in possible_hazards:
        add_remove_hazard_button.possible_hazards.append_entry()
    possible_hazards_tuple = zip(possible_hazards, add_remove_hazard_button.possible_hazards)
    for possible_hazard, hazard_button in possible_hazards_tuple:
        hazard_button.hazard_id.data = possible_hazard.id
    return render_template('hca/add_hazard.html', current_hazards_tuple=current_hazards_tuple,
                           possible_hazards_tuple=possible_hazards_tuple, hidden=add_remove_hazard_button)


def write():
    # TODO relationships do not delete
    project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
    project_db_session.query(HCA).delete()
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
    if not remaining_columns:
        return path
    for payload in remaining_columns[0].pmvvs:
        if not remaining_columns[1:]:
            result.append(recursive(remaining_columns[1:], path + [payload], result))
        else:
            recursive(remaining_columns[1:], path + [payload], result)
    return result
