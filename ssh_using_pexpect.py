import getpass
from pexpect import pxssh

devices = {'Switch3750': {'prompt1': 'Lab-Switch3750-X>', 'prompt2': 'Lab-Switch3750-X#', 'ip': '172.18.0.2'}}
commands = ['terminal length 0', 'show version', 'show run']

username = input('Username: ')
password = input('Password: ')

# Starts the loop for devices
for device in devices.keys():
    outputFileName = device + '_output.txt'
    # user mode prompt
    device_prompt1 = devices[device]['prompt1']
    # privilege mode prompt
    device_prompt2 = devices[device]['prompt2']
    child = pxssh.pxssh()
    child.login(devices[device]['ip'],
                username.strip(),
                password.strip(),
                auto_prompt_reset=False)
    print("I've logged in. Elevating to privilege mode.\n")
    child.sendline('enable')
    child.expect('Password:')
    child.sendline('VMware1!')
    child.expect(device_prompt2)
    print("Successfully evelvated to privilege mode!\n")

    index = 1

    # starts the loop for commands and write to output
    with open(outputFileName, 'wb') as f:
        for command in commands:
            print(f"sending command {index}")
            child.sendline(command)
            child.expect(device_prompt2)
            f.write(child.before)
            index += 1

    child.logout()


