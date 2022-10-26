# This script will implement code from page 60

import paramiko, time


def clear_buffer(connection, max_buffer=5000):
    if connection.recv_ready():
        return connection.recv(max_buffer)


device = {'Lab-Switch3750-X': {'ip': '172.18.0.2'}}
commands = ['terminal length 0\n', 'show ip interface brief\n', 'enable\n', 'VMware1!\n', 'show version\n']

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sleep_time = 1

connection.connect(device['Lab-Switch3750-X']['ip'],
                   username='vmware',
                   password='VMware1!',
                   look_for_keys=False,
                   allow_agent=False
                   )

new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output.decode('ASCII'))
clear_buffer(new_connection)

new_connection.send(commands[0])
clear_buffer(new_connection)

new_connection.send(commands[1])
time.sleep(sleep_time)
output = new_connection.recv(5000)
print(output.decode('ASCII'))
clear_buffer(new_connection)

new_connection.send(commands[2])
time.sleep(sleep_time)
output = new_connection.recv(5000)
print(output.decode('ASCII'))
clear_buffer(new_connection)

new_connection.send(commands[3])
time.sleep(sleep_time)
output = new_connection.recv(5000)
print(output.decode('ASCII'))
clear_buffer(new_connection)

new_connection.send(commands[4])
time.sleep(sleep_time)
output = new_connection.recv(5000)
print(output.decode('ASCII'))
clear_buffer(new_connection)
