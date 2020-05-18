# usermgmt

Required modules to install for setup
Using Python 3.7.7
* [python3 version](https://www.python.org/downloads/release/python-377/)
* pip install argparse
* pip install passlib
* pip install paramiko
* pip install pathlib
* pip install scpclient
* pip install ansible

Using python
============
All python scripts have a usage description for the arguments required.  The usage message can be displayed by typing at the command line prompt:  

`python3 script_name.py -h`

- add user - add.py
    - required parameters for adding a user are:  
    -u USERNAME           username for accessing host  
    -n HOSTNAME           hostname where user is to be added 
    -k PUB_KEY_PATH_FILE  file path and name, to the key   
    -a ADD_USER           Username to add  
    
    - optional pararamters for adding a user are:
    -g GROUP_ID           group id for new user  
    -c FULL_NAME          comments like user full name  
    -i USER_ID            user id for the new user 
    
    - the default parameter for adding a user is:  
    -p PASSWORD           new user password  

- remove user - remove.py
    - required parameters for deleting a user are:  
    -u USERNAME           username for accessing host  
    -n HOSTNAME           hostname where user is to be deleted 
    -k PUB_KEY_PATH_FILE  file path and name, to the key   
    -a DEL_USER           Username to delete  
    
- list users - list.py
    - required parameters for listing users:  
    -u USERNAME           username for accessing host  
    -n HOSTNAME           hostname where users are to be listed
    -k PUB_KEY_PATH_FILE  file path and name, to the key   

Example:  
`$ python3 add.py -u=ec2-user -n=hostname.com -k=/Users/nico/Desktop/virginia.pem -a=eabern2 -c='Erica Abernathy' -i=601 -g=10`


Using ansible
=============

change directory into users folder
`$ cd users`
`$ ansible-playbook yaml_file.yml --private-key=/path/to/file/key.pem`

- add user - create_users.yml
To add users on the host, edit the create_users.yml file by adding the users name under 'loop:' of the file.  
 loop:  
        - { name: 'user1', comment: 'User One' }  
        - { name: 'user2', comment: 'User Two' }  
        - { name: 'user3', comment: 'User Three' }  
        - { name: 'user4', comment: 'User Four' }
        
- remove user - remove_users.yml
- list users - list_users.yml
