# Alex Diker
# Instructions :
#
# Take automated backups of our network devices (switches, routers, wireless controllers)
#
#

import paramiko
import time
from getpass import getpass

username = 'cccc'
password = 'cccc'


DEVICE_LIST = open('2020-devices')  # open device list
for RTR in DEVICE_LIST:
    RTR = RTR.strip()
    print("\n *** INFO:")
    print("\n *** Connecting to device: " + RTR + '*****\n') # show you are connecting to device
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # add and show ssh connections/enter credentials
    SESSION.connect(RTR,port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,
                    allow_agent=False)

    DEVICE_ACCESS = SESSION.invoke_shell()
    DEVICE_ACCESS.send(b'|')

    time.sleep(1)
    output = DEVICE_ACCESS.recv(65000)
    print(output.decode('ascii'))

    SESSION.close()
