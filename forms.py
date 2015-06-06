from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError, validators, RadioField, SelectField
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

def get_users():
	users_existing_cmd_string='cut -d: -f1 /etc/passwd'
	users_existing_cmd = shlex.split(users_existing_cmd_string)
	process=subprocess.Popen(users_existing_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	users_str,err=process.communicate()
	users_list = users_str.splitlines()
	return users_list

def get_user_for_select_field():
	users_list=get_users()
	user_for_select_field=[]
	for user in users_list:
		choice_tuple=(user,user)
		user_for_select_field.append(choice_tuple)
	return user_for_select_field

class linux_operation_add_or_mod_form(Form):
	username = StringField("username", [validators.Required("Please enter the user name")])
	password = PasswordField("password", [validators.Required("Please enter the Password")])
	shell_selection = RadioField(u"Default Shell?",choices=obtain_list_shells())
	root_privilege = RadioField(u"Root privilege?",choices=[('y','yes'),('n','no')])

class linux_operation_del_form(Form):
	#username = StringField("username", [validators.Required("Please enter the user name")])
	username=SelectField(u'Choose Username',choices=get_user_for_select_field())
	submit = SubmitField("DELETE USER")

