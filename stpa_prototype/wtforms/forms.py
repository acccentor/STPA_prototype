from wtforms import Form, StringField, SubmitField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired


# class VCSButtons(Form):


class GoalForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the goal'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the goal'})
    submit_goal = SubmitField(label='Create Goal')


class ShowUpdate(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the goal'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the goal'})
    create_goal = SubmitField(label='Create Goal')


class HazardForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the hazard'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the hazard'})
    submit_hazard = SubmitField(label='Create Hazard')


class PMVVForm(Form):
    text = StringField(render_kw={"placeholder": 'Please name pmv value'}, validators=[DataRequired()])


class PMVForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the pmv'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the pmv'})
    submit_pmv = SubmitField(label='Create PMV')
    submit_pmvv = SubmitField(label='Add PMV Value')
    pmvvs = FieldList(FormField(PMVVForm), min_entries=1)


class ControlActionForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the ca'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the ca'})
    submit_ca = SubmitField(label='Create control action')


class HCAAddHazard(Form):
    add_cah = SubmitField(label='+')
    add_cahtl = SubmitField(label='+')
    add_cahte = SubmitField(label='+')
    add_cahnp = SubmitField(label='+')


class CAHazard(Form):
    hazards = FieldList(FormField(HCAAddHazard))