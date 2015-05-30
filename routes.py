from flask import Flask, render_template, request
from forms import linux_operation_form 

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
 form = linux_operation_form()
 
 if request.method == 'POST':
  return 'form posted'
 elif request.method == 'GET':
  return render_template('add_user.html',form = form)

if __name__=='__main__':
	app.run(host="0.0.0.0", debug=True)


