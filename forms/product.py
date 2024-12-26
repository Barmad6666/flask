from wtforms import Form, StringField, validators, IntegerField, FloatField,BooleanField
class ProductForm(Form):
    name = StringField('name', [validators.Length(min=3, max=25)])
    num_available = StringField('num_available')
    price = StringField('price', [validators.Length(min=3, max=25)])
    weight = StringField('weight')
    description = StringField('description', [validators.Length(min=3, max=250)])
    image_url = StringField('image_url', [validators.Length(min=3, max=25)])