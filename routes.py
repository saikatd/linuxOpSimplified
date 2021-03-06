from flask import Flask, render_template, request, flash
from forms import * 
from user_manipulation import *

app=Flask(__name__)

app.secret_key = 'development key'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/add_user',methods=['GET','POST'])
def add_user():
 #form that contains the create user fields
 #username, password, shell of choice, root_privilege
 form = linux_operation_add_or_mod_form()
 
 if request.method == 'POST':
 	if form.validate() == False:
 		return render_template('add_user.html', form=form)
 	else:

 		username=form.username.data
 		password=form.password.data
 		shell_selection=form.shell_selection.data
 		root_privilege=form.root_privilege.data
 		status=func_add_user(username, password,shell_selection,root_privilege)
 		if status == 0:
 			return render_template('home.html')
 		if status == 1:
 			error = "user already exists"
 			return render_template('error_page.html', error=error)
	  		
 elif request.method == 'GET':
 	return render_template('add_user.html',form = form)

@app.route('/del_user',methods=['GET','POST'])
def del_user():
 #form that contains the delete user fields
 #username only
 form = linux_operation_del_form()
 
 if request.method == 'POST':
 	if form.validate() == False:
 		return render_template('del_user.html', form=form)
 	else:
 		username=form.username.data
 		status = func_del_user(username)
 		if status == 0:
 			return render_template('home.html')
 		else:
 			error = "user does not exist"
 			return render_template('error_page.html', error=error)

 elif request.method == 'GET':
  return render_template('del_user.html',form = form)


@app.route('/mod_user',methods=['GET','POST'])
def mod_user():
	#form contains the 
	# username, password, shell of choice, root privilege
	form = linux_operation_add_or_mod_form()
	if request.method == 'POST':
	 	if form.validate() == False:
	 		return render_template('mod_user.html', form=form)
	 	else:

	 		username=form.username.data
	 		password=form.password.data
	 		shell_selection=form.shell_selection.data
	 		root_privilege=form.root_privilege.data
	 		status=func_mod_user(username,password,shell_selection,root_privilege)
	 		if status == 0:
	 			return render_template('home.html')
	 		if status == 1:
	 			error = "user does not exists"
	 			return render_template('error_page.html', error=error)
	  		
	elif request.method == 'GET':
			return render_template('mod_user.html',form = form)

if __name__=='__main__':
	app.run(host="0.0.0.0", debug=True)


