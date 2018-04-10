from flask import Blueprint, render_template, request, url_for, redirect
# from flask import current_app as app
# from stpa_prototype import Todo
from stpa_prototype.database.database import db_session
from stpa_prototype.database.models import Hazard
from flask_security.decorators import login_required

hazards_blueprint = Blueprint('hazards', __name__, template_folder='templates', url_prefix='/hazards')


@hazards_blueprint.route('/hello')
def hello_world():
    return 'Hello!!!! Werld!'


@hazards_blueprint.route('/')
@login_required
def index():
    return render_template('fundamentals/hazards/index.html',
                           hazards=Hazard.query.order_by(Hazard.id.asc()).all()
                           )


@hazards_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        hazards = Hazard(request.form['title'], request.form['text'])
        db_session.add(hazards)
        db_session.commit()
        return redirect(url_for('hazards.index'))
    return render_template('fundamentals/hazards/new.html')


@hazards_blueprint.route('/<hazard_id>', methods=['GET', 'POST'])
@login_required
def show_or_update(hazard_id):
    hazard_item = Hazard.query.get(hazard_id)
    if request.method == 'GET':
        return render_template('fundamentals/hazards/view.html', hazard=hazard_item)
    hazard_item.title = request.form['title']
    hazard_item.text = request.form['text']
    hazard_item.vcs_check = ('vcs_check.%d' % hazard_id) in request.form
    db_session.commit()
    return redirect(url_for('hazards.index'))
