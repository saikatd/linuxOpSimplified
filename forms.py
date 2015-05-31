from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError, validators

class linux_operation_form(Form):
 username = StringField("username", [validators.Required("Please enter the user name")])
 password = PasswordField("password", [validators.Required("Please enter the Password")])
 submit = SubmitField("CREATE")

