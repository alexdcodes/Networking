import os
import paramiko
import sys
import time

hostname = "hostip"
Meh = "Mehip"
MehUN = "YourUsername"
MehPW = "YourPassword"
waittime = "WaitTimeInSeconds"

PingMeh = os.system("ping -c 1 -w2 " + Meh + " > /dev/null 2>&1")
PingHOST = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")

if PingHOST == 0:
    print('Host online')
    sys.exit()
else:
    if PingMeh == 0:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            Meh,
            port=22,
            username=MehUN,
            password=MehPW,
            look_for_keys=False
            )
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
            'racadm serveraction powerup'
            )
        print('Starting host')
    else:
        print('Meh down!')
        sys.exit()