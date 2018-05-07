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

