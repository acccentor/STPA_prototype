from flask import Flask, redirect, url_for
from flask_security import Security, SQLAlchemySessionUserDatastore

from stpa_prototype.auth.auth import auth_blueprint
from stpa_prototype.database.database import db_session, init_db
from stpa_prototype.database.models import User, Role
from stpa_prototype.fundamentals.control_actions import ca_blueprint
from stpa_prototype.fundamentals.goals import goals_blueprint
from stpa_prototype.fundamentals.hazards import hazards_blueprint
from stpa_prototype.fundamentals.pmv import pmv_blueprint
from stpa_prototype.hca.hca import hca_blueprint
from stpa_prototype.project_management.project import project_blueprint
from stpa_prototype.project_management.vcs_blueprint import vcs_blueprint

app = Flask(__name__)

app.config.from_pyfile('../config.py')

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

app.register_blueprint(goals_blueprint)
app.register_blueprint(hazards_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(project_blueprint)
app.register_blueprint(vcs_blueprint)
app.register_blueprint(pmv_blueprint)
app.register_blueprint(ca_blueprint)
app.register_blueprint(hca_blueprint)


@app.route('/')
def hello_world():
    return redirect(url_for('auth.login'))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


