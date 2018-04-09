from flask import Blueprint, render_template, request, url_for, redirect
from stpa_prototype.database import db_session
import stpa_prototype

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        stpa_prototype.user_datastore.create_user(email=request.form['email'], password=request.form['password'])
        db_session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return 'Hello!!!! Werld!'
    # if request.method == 'POST':
    #     # stpa_prototype.user_datastore.create_user(email=request.form['email'], password=request.form['password'])
    #     return redirect(url_for('goals.index'))
    # return render_template('auth/login.html')



# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     for
