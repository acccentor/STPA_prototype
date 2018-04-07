from flask import Blueprint, render_template, request, url_for, redirect
from stpa_prototype import user_datastore

auth_blueprint = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        user_datastore.create_user(email=request.form['email'], password=request.form['password'])
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')



# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     for
