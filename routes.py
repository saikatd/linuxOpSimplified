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
 #username, password
 form = linux_operation_add_form()
 
 if request.method == 'POST':
 	if form.validate() == False:
 		return render_template('add_user.html', form=form)
 	else:

 		username=form.username.data
 		password=form.password.data
 		func_add_user(username, password)
 		
	  		
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
 		func_del_user(username)
 			  		
 elif request.method == 'GET':
  return render_template('del_user.html',form = form)


if __name__=='__main__':
	app.run(host="0.0.0.0", debug=True)


