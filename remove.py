import argparse, subprocess, paramiko

def sshConnect(args):
	command = "sudo userdel -fr"
	addition = ''.join(args.del_user)

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname = args.hostname, 
		username = args.username, 
		pkey = paramiko.RSAKey.from_private_key_file(args.pub_key_path_file) )
	
	stdin, stdout, stderr = ssh.exec_command('{} {}'.format(command, addition), bufsize=-1, timeout=None, get_pty=False)

	print(stdout.read())
	print(stdout.read())

	ssh.close()


def deleteFile():
	file_to_rem = pathlib.Path("passwd")
	file_to_rem.unlink()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog='PROG',
									description='Enter the host name or ip address, username and the public key file path and name\n \
									python3 PROG.py -u=username -n=hostname -k=/path/to/key.pem')
	parser.add_argument('-u', type=str, help='What is the username', dest='username', required=True)
	parser.add_argument('-n', type=str, help='the hostname', dest='hostname', required=True)
	parser.add_argument('-k', type=str, help='What is the file path and name, to the key', dest='pub_key_path_file', required=True)
	parser.add_argument('-d', type=str, help='Username to delete', dest='del_user', required=True)
    
	args = parser.parse_args()

	sshConnect(args)
	


	

