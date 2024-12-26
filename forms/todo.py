from wtforms import Form, StringField, validators
class TodoForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=50)])
    description = StringField('Description', [validators.Length(min=0, max=1000)])