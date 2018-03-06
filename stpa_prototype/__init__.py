from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, abort
from stpa_prototype.fundamentals.goals import goals_blueprint
from stpa_prototype.database import db_session

app = Flask(__name__)

app.config.from_pyfile('../config.py')
app.db = SQLAlchemy(app)

app.register_blueprint(goals_blueprint)


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
