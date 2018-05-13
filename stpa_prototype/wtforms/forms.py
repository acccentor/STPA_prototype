from wtforms import Form, StringField, SubmitField, TextAreaField
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


class PMVForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the pmv'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the pmv'})
    submit_pmv = SubmitField(label='Create PMV')


class ControlActionForm(Form):
    title = StringField(render_kw={"placeholder": 'Please give title to the ca'}, validators=[DataRequired()])
    text = TextAreaField(render_kw={"placeholder": 'Describe the ca'})
    submit_ca = SubmitField(label='Create control action')
