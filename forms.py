from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError, validators, RadioField
import subprocess,shlex

def obtain_list_shells():
	#obtaining the shells from the existing server
	shell_choices=[]
	cmd_string='cat /etc/shells'
	cmd=shlex.split(cmd_string)
	process=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err=process.communicate()
	bashes = out.splitlines()
	bashes.pop(0)
	for shells in bashes:
		choice_tuple=(shells,shells)
		shell_choices.append(choice_tuple)
	return shell_choices 

class linux_operation_add_form(Form):
	username = StringField("username", [validators.Required("Please enter the user name")])
	password = PasswordField("password", [validators.Required("Please enter the Password")])
	
	
	shell_selection = RadioField(u"Default Shell?",choices=obtain_list_shells())
 	
 	submit = SubmitField("CREATE USER")

class linux_operation_del_form(Form):
	username = StringField("username", [validators.Required("Please enter the user name")])
	submit = SubmitField("DELETE USER")

