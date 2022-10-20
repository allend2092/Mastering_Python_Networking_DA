import pexpect


# page 50 - this is some kind of check to make sure the package can be used.
print(dir(pexpect))


# login to device from linux. on older networking gear, might need to allow older cypher suits
# home/<user>/.ssh should have a file named config
# Host <ip address>
# 	KexAlgorithms +diffie-hellman-group1-sha1
#
# Connect to networking device
child = pexpect.spawn('ssh vmware@172.18.0.2')

# What should we expect as the prompt after sending a command?
child.expect('Password:', timeout=5)

# Send password
child.sendline('VMware1!')

# What should we expect as the prompt after sending a command?
child.expect('Lab-Switch3750-X>')

# Send command
child.sendline('terminal length 0')

# What should we expect as the prompt after sending a command?
child.expect('Lab-Switch3750-X>')

# Send command
child.sendline('show ip interface brief')

# Print some of the output. Output is initially a byte string. Must be converted to string

# print the child object for more information about it
print(child)
print()
child.expect('Lab-Switch3750-X>')
# print the child object for more information about it
print(child)
print()
print(child.before)
print(child.after)

response = child.before.decode('ASCII')
print('\n ' + response)

response = child.after.decode('ASCII')
print('\n ' + response)


# Additional pexpect features. Create log file for debug
child.logfile = open('debug', 'wb')

