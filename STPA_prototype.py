from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, abort

app = Flask(__name__)

app.config.from_pyfile('wsgi/stpa_prototype.cfg')
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'system_goals'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    vcs_check = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()


@app.route('/')
def hello_world():
    return 'Hello World!'


def index():
    return render_template('index.html',
                           todos=Todo.query.order_by(Todo.pub_date.desc()).all()
                           )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        todo = Todo(request.form['title'], request.form['text'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

if __name__ == '__main__':
    app.run()
