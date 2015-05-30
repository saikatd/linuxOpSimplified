from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField

class linux_operation_form(Form):
 username = StringField("username")
 password = PasswordField("password")
 submit = SubmitField("Send")

