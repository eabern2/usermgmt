import argparse, subprocess, paramiko, pathlib
from scp import SCPClient

def sshConnect(args):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname = args.hostname, 
		username = args.username, 
		pkey = paramiko.RSAKey.from_private_key_file(args.pub_key_path_file) )
	scp = SCPClient(ssh.get_transport())

	scp.get('/etc/passwd')
	scp.close()
	ssh.close()


def deleteFile():
	file_to_rem = pathlib.Path("passwd")
	file_to_rem.unlink()


if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog='PROG',
									description='Enter the host name or ip address, username and the public key file path and name\n \
									python3 python.py -u=username -n=hostname -k=/path/to/key.pem')
	parser.add_argument('-u', type=str, help='What is the username', dest='username', required=True)
	parser.add_argument('-n', type=str, help='What is the hostname', dest='hostname', required=True)
	parser.add_argument('-k', type=str, help='keyfile path and name', dest='pub_key_path_file', required=True)
    
	args = parser.parse_args()

	sshConnect(args)
	subprocess.run("awk -F: '{ if(($3 >= 500)&&($3 <65534)) print $1, $3, $5 }' passwd", shell=True)
	deleteFile()


	

