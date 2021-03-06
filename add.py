import argparse, subprocess, paramiko

def sshConnect(command, args):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname = args.hostname, 
		username = args.username, 
		pkey = paramiko.RSAKey.from_private_key_file(args.pub_key_path_file) )
	
	stdin, stdout, stderr = ssh.exec_command('{}'.format(command), bufsize=-1, timeout=None, get_pty=False)
	print(stderr.read())
	ssh.close()


def createNewUser(args):
	command = '{} {}'.format("sudo useradd", args.add_user)    

	if(args.full_name):
		command = command + " -c '" + args.full_name + "'"
	if(args.user_id):
		command = command + " -u " + args.user_id 
	if(args.group_id):
		command = command + " -g " + args.group_id 
	sshConnect(command, args)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog='PROG',
									description='Enter the host name or ip address, username and the public key file path and name\n \
									python3 PROG.py -u=username -n=hostname -k=/path/to/key.pem -a=user_being_added -g=group_id -i=user_id\n \
									-c=comments')
	parser.add_argument('-u', type=str, help='username accessing host', dest='username', required=True)
	parser.add_argument('-n', type=str, help='the hostname', dest='hostname', required=True)
	parser.add_argument('-k', type=str, help='What is the file path and name, to the key', dest='pub_key_path_file', required=True)
	parser.add_argument('-a', type=str, help='Username to add', dest='add_user', required=True)
	parser.add_argument('-g', type=str, help='group id for new user', dest='group_id')
	parser.add_argument('-c', type=str, help='comments like user full name', dest='full_name')
	parser.add_argument('-i', type=str, help='user id for the new user', dest='user_id')
	parser.add_argument('-p', type=str, help='new user password', dest='password', default='changeMe1')
    
	args = parser.parse_args()
	createNewUser(args)	


	

