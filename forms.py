from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError

class linux_operation_form(Form):
 username = StringField("username", [validators.Required("Please enter the username"), validators.Length(min=4, max=25,message="username should be Min 4 and max 25 chars")])
 password = PasswordField("password" [validators.Required("Please enter the password"), validators.Length(min=4, max=25,message="password should be Min 4 and max 25 chars")])
 submit = SubmitField("CREATE")

