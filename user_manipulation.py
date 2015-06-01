import subprocess,shlex

def func_add_user(username,password):
	
	cmd_string='sudo useradd -m '+username
	cmd=shlex.split(cmd_string)
	process=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process.communicate()

def func_del_user(username):
	
	cmd_string='sudo userdel -r '+username
	cmd=shlex.split(cmd_string)
	process=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	process.communicate()