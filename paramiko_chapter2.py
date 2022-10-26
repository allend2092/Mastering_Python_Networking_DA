# This script will implement code from page 60

import paramiko, time

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('172.18.0.2', username='vmware', password='VMware1!', look_for_keys=False, allow_agent=False)
new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output.decode('ASCII'))

new_connection.send('terminal length 0\n')

new_connection.send('show ip interface brief\n')
time.sleep(2)
output = new_connection.recv(5000)
print(output.decode('ASCII'))
