import subprocess,shlex
import crypt

def if_user_exists(username):
	users_existing_cmd_string='cut -d: -f1 /etc/passwd'
	users_existing_cmd = shlex.split(users_existing_cmd_string)
	process=subprocess.Popen(users_existing_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	users_str,err=process.communicate()
	users_list = users_str.splitlines()
	if username in users_list:
		return 1

def func_add_user(username,password,shell_selection):
	if if_user_exists(username) != 1:
		encPass = crypt.crypt(password,"22")
		cmd_string='sudo useradd -m -p '+encPass+' -s '+shell_selection+' '+username
		cmd=shlex.split(cmd_string)
		process=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate()
		return 0
	else:
		return 1

def func_del_user(username):
	if if_user_exists(username) == 1:
		cmd_string='sudo userdel -r '+username
		cmd=shlex.split(cmd_string)
		process=subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		process.communicate()
		return 0
	else:
		return 1