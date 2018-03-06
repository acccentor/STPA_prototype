from flask import Blueprint, render_template, request, url_for, redirect
# from flask import current_app as app
# from stpa_prototype import Todo
from stpa_prototype.database import db_session
from stpa_prototype.models import hazards
hazards_blueprint = Blueprint('hazards', __name__, template_folder='templates', url_prefix='/hazards')


@hazards_blueprint.route('/hello')
def hello_world():
    return 'Hello!!!! Werld!'


@hazards_blueprint.route('/')
def index():
    return render_template('fundamentals/hazards/index.html',
                           hazards=hazards.query.order_by(hazards.id.asc()).all()
                           )


@hazards_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        hazards = Hazard(request.form['title'], request.form['text'])
        db_session.add(hazards)
        db_session.commit()
        return redirect(url_for('hazards.index'))
    return render_template('fundamentals/hazards/new.html')


@hazards_blueprint.route('/<int:todo_id>', methods=['GET', 'POST'])
def show_or_update(todo_id):
    hazard_item = hazards.query.get(todo_id)
    if request.method == 'GET':
        return render_template('fundamentals/hazards/view.html', todo=hazard_item)
    hazard_item.title = request.form['title']
    hazard_item.text = request.form['text']
    hazard_item.vcs_check = ('vcs_check.%d' % todo_id) in request.form
    db_session.commit()
    return redirect(url_for('hazards.index'))
