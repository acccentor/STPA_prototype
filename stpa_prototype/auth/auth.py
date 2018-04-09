from flask_security import utils
from flask import Blueprint, render_template, request, url_for, redirect
from stpa_prototype.database import db_session
from stpa_prototype import User
import stpa_prototype

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        stpa_prototype.user_datastore.create_user(email=request.form['email'],
                                                  password=utils.hash_password(request.form['password']))
        db_session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db_session.query(User).filter_by(email=request.form['email']).first()
        print utils.verify_password(request.form['password'], user.password)
        # temp_user = stpa_prototype.user_datastore.get_user(request.form['email'])
        # print utils.verify_and_update_password(request.form['password'], temp_user)
        # print utils.hash_password(request.form['password'])
        # print utils.verify_and_update_password(utils.hash_password(request.form['password']), temp_user)
    return render_template('auth/login.html')

# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     for
