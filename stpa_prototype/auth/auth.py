from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_security import utils

import stpa_prototype
from stpa_prototype.database.database import db_session
from stpa_prototype.database.models import User

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        stpa_prototype.user_datastore.create_user(email=request.form['email'],
                                                  password=utils.hash_password(request.form['password']))
        db_session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


# TODO check user before comparing password, throws error when invalid user
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db_session.query(User).filter_by(email=request.form['email']).first()
        if utils.verify_password(request.form['password'], user.password):
            utils.login_user(user, remember=None)
            # TODO more dynamic project select
            session['active_project_db'] = 1
            return redirect(url_for('project.index'))
        # temp_user = stpa_prototype.user_datastore.get_user(request.form['email'])
        # print utils.verify_and_update_password(request.form['password'], temp_user)
        # print utils.hash_password(request.form['password'])
        # print utils.verify_and_update_password(utils.hash_password(request.form['password']), temp_user)
    return render_template('auth/login.html')


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    utils.logout_user()
    return redirect(url_for('auth.login'))


# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     for
