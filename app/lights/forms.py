from flask_wtf import Form
from wtforms import SelectField, StringField, SubmitField

class LightsForm(Form):
  type = SelectField('Type"', choices=[('forwards', 'Forwards'), ('backwards', 'Backwards'), ('illinois', 'Illinois (Animation)'), ('rainbow', 'Rainbow (Animation)')])
  light_one = StringField("light_one")
  light_two = StringField("light_two")
  light_three = StringField("light_three")
  light_four = StringField("light_four")
  light_five = StringField("light_five")
  light_six = StringField("light_six")
  light_seven = StringField("light_seven")
  delay = StringField("delay")
  submit = SubmitField("Send")