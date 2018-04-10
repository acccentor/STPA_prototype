from flask_security import Security, SQLAlchemySessionUserDatastore
from flask import Flask, render_template, abort


from stpa_prototype.database import db_session, init_db
from stpa_prototype.models import User, Role

from stpa_prototype.auth.auth import auth_blueprint
from stpa_prototype.fundamentals.goals import goals_blueprint
from stpa_prototype.fundamentals.hazards import hazards_blueprint
from stpa_prototype.fundamentals.project import project_blueprint

app = Flask(__name__)

app.config.from_pyfile('../config.py')
# app.db = SQLAlchemy(app)

# Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

# # Flask-Login
# login_manager = LoginManager()

app.register_blueprint(goals_blueprint)
app.register_blueprint(hazards_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(project_blueprint)


init_db()

# # Login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# # move later?
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


# class Todo(app.db.Model):
#     __tablename__ = 'system_goals'
#     id = app.db.Column('todo_id', app.db.Integer, primary_key=True)
#     title = app.db.Column(app.db.String(60))
#     text = app.db.Column(app.db.String)
#     vcs_check = app.db.Column(app.db.Boolean)
#     pub_date = app.db.Column(app.db.DateTime)
#
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text
#         self.vcs_check = False
#         self.pub_date = datetime.utcnow()


# @app.route('/')
# def index():
#     return render_template('index.html', todos=Todo.query.order_by(Todo.id.asc()).all())


@app.route('/')
def hello_world():
    return 'Hello!!!! Werld!'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# if __name__ == '__main__':
#     app.run()
