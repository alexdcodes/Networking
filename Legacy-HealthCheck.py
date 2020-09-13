import paramiko
import time
import getpass

print("""
********************************************************************************************
Alex Diker - Project from 2019 
********************************************************************************************
""")

device_type = input("""
INFO:  Devices Available:\n \n***  Check ***\n
[ PRE-CHECKS  ] Cisco XXX Router, Cisco XXX Switch, NX-Extreme Wireless Controller  [1] 
[ PRE-CHECKS  ] Cisco XXX Router, Cisco XXX Switch, NX-Extreme Wireless Controller  [2] 
[ POST-CHECKS ] Cisco XXX Router, Cisco XXX Switch, NX-Extreme Wireless Controller [3]
[ POST-CHECKS ] ENCS–vEdge–VNF, Cisco XXX Switch, NX-Extreme Controller [4]
  \n*** XXX Check ***\n 
[ PRE-CHECKS  ] Router-XXXX-Legacy, Cisco XXX Switch, NX-Extreme Wireless Controller  [5] 
[ POST-CHECKS ] Router-XXXX-POST, Cisco XXX Switch, NX-Extreme Wireless Controller [6]
  \n*** Operational Checks ***\n
[ DIAGNOSTIC-CHECKS ] COMPARE CHECKER [7]
\nINFO:  Select Test: """)

if device_type == "1":
    print("\n")
    store_number = input("INFO: Enter the store number: ")
    ip1 = input("INFO: Cisco XXX Router: Enter the IP:  ")
    ip2 = input("INFO: Cisco XXXX Switch: Enter The IP:  ")
    ip3 = input("INFO: Wireless Controller: Enter the IP: ")
    username = input("What is your username: ")
    password = getpass.getpass(prompt="Enter your password?: ")

# Cisco 2911 Router Connection and Settings

    print("\nINFO: You are connecting to ", ip1, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(99535)


    ssh_conn.send("show int GigabitEthernet0/0 \n")
    time.sleep(1)
    ssh_conn.send("\n show ip ospf database \n")
    time.sleep(1)
    ssh_conn.send("\n show ip route ospf \n")
    time.sleep(2)
    ssh_conn.send("\n show ip bgp sum \n")
    time.sleep(1)
    ssh_conn.send(" show dmvpn \n")
    time.sleep(1)
    ssh_conn.send(" show ip route bgp \n")
    time.sleep(1)
    ssh_conn.send(" ping \n")
    time.sleep(1)
    ssh_conn.send(" show run int di0 \n")
    time.sleep(1)
    ssh_conn.send(" show int desc | i up / show int desc | i down \n")
    time.sleep(1)
    ssh_conn.send("show ip arp \n")
    time.sleep(1)
    ssh_conn.send("\n exit \n")
    time.sleep(1)

    output_lr = ssh_conn.recv(99535)
    print(output_lr.decode('utf-8'))
    print("\n\n")


    time.sleep(2)
    print("\nINFO: Connecting to Next Device.")
    print("\nINFO: You are connecting to ", ip2, "\n")
    time.sleep(1)
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip2, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output2 = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output_sw = ssh_conn_sw.recv(77535)
    print(output_sw.decode('utf-8'))


    time.sleep(2)
    print("Connecting to Next Device.\n\n")
    print(""" INFO: You need to enter a different username and password for the
    NX-Extreme Wireless Controller
    \n""")
    username2 = input("What is your username : ")
    password2 = getpass.getpass(prompt="Enter your password?: ")
    print("\nINFO: You are connecting to ", ip3, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip3, port=22, username=username2,
                         password=password2,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_nx = pre_ssh_conn.invoke_shell()
    banner_output3 = ssh_conn_sw.recv(89935)

    ssh_conn_nx.send("show global device-list | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nshow wireless ap on LS01005\n R")
    time.sleep(3)
    ssh_conn_nx.send("\nshow wireless client on LS01005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption status | i 1005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption offline | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nexit\n")
    time.sleep(1)

    output_nx = ssh_conn_sw.recv(89935)
    print(output_nx.decode('utf-8'))


    lg = "C:/Users/" + username + "/Desktop/[1]pre-check-" + username + "-" + ip1 + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
    print("\nLog file Created: " + lg)
    time.sleep(5)


elif device_type == "2":
    print("\n")
    store_number = input("INFO: Enter the store number: ")
    ip1 = input("INFO: Cisco XXX Router: Enter the IP:  ")
    ip2 = input("INFO: Cisco XXX Switch: Enter The IP:  ")
    ip3 = input("INFO: NX-Extreme Wireless Controller: Enter the IP: ")
    username = input("What is your username: ")
    password = getpass.getpass(prompt="Enter your password?: ")


    print("\nINFO: You are connecting to ", ip1, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(65535)


    ssh_conn.send("show int GigabitEthernet0/0 \n")
    time.sleep(1)
    ssh_conn.send("show ip ospf database\n")
    time.sleep(1)
    ssh_conn.send("show ip route ospf\n")
    time.sleep(1)
    ssh_conn.send("show ip bgp sum\n")
    time.sleep(1)
    ssh_conn.send("show dmvpn\n")
    time.sleep(1)
    ssh_conn.send("show ip route bgp\n")
    time.sleep(1)
    ssh_conn.send("ping \n")
    time.sleep(1)
    ssh_conn.send("show run int di0\n")
    time.sleep(1)
    ssh_conn.send("show int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn.send("show ip arp\n")
    time.sleep(1)
    ssh_conn.send("\nexit\n")
    time.sleep(1)

    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))
    print("\n\n")


    time.sleep(2)
    print("Connecting to Next Device.")
    print("\nINFO: You are connecting to ", ip2, "\n")
    time.sleep(1)
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip2, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output2 = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output_sw = ssh_conn_sw.recv(77535)
    print(output_sw.decode('utf-8'))


    time.sleep(2)
    print("Connecting to Next Device.\n\n")
    print(""" INFO: You need to enter a different username and password for the
        NX-Extreme Wireless Controller
        \n""")
    username2 = input("What is your username : ")
    password2 = getpass.getpass(prompt="Enter your password?: ")
    print("\nINFO: You are connecting to ", ip3, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip3, port=22, username=username2,
                         password=password2,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_nx = pre_ssh_conn.invoke_shell()
    banner_output3 = ssh_conn_sw.recv(89935)

    ssh_conn_nx.send("show global device-list | i XXX\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nshow wireless ap on XXXX\n R")
    time.sleep(3)
    ssh_conn_nx.send("\nshow wireless client on XXXX\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption status | i XXXX\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption offline | i XXXXX\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nexit\n")
    time.sleep(1)

    output_nx = ssh_conn_sw.recv(89935)
    print(output_nx.decode('utf-8'))


    lg = "C:/Users/" + username + "/Desktop/[2]pre-check-" + username + "-" + ip1 + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
    print("\nLog file Created: " + lg)
    time.sleep(5)

elif device_type == "3":
    print("\n")
    store_number = input("INFO: Enter the store number: ")
    ip1 = input("INFO: Cisco XX Router: Enter the IP:  ")
    ip2 = input("INFO: Cisco XX Switch: Enter The IP:  ")
    ip3 = input("INFO: NX-Extreme Wireless Controller: Enter the IP: ")
    username = input("What is your username: ")
    password = getpass.getpass(prompt="Enter your password?: ")


    print("\nINFO: You are connecting to ", ip1, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(65535)


    ssh_conn.send("show int GigabitEthernet0/0 \n")
    time.sleep(1)
    ssh_conn.send("show ip ospf database\n")
    time.sleep(1)
    ssh_conn.send("show ip route ospf\n")
    time.sleep(1)
    ssh_conn.send("show ip bgp sum\n")
    time.sleep(1)
    ssh_conn.send("show dmvpn\n")
    time.sleep(1)
    ssh_conn.send("show ip route bgp\n")
    time.sleep(1)
    ssh_conn.send("ping \n")
    time.sleep(1)
    ssh_conn.send("show run int di0\n")
    time.sleep(1)
    ssh_conn.send("show int desc | i up / show int desc | i down\n")
    time.sleep(1)
    time.sleep(1)
    ssh_conn.send("show ip arp\n")
    ssh_conn.send("\nexit\n")
    time.sleep(1)

    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))
    print("\n\n")


    time.sleep(2)
    print("Connecting to Next Device.")
    print("\nINFO: You are connecting to ", ip2, "\n")
    time.sleep(1)
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip2, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output2 = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nRouter\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output_sw = ssh_conn_sw.recv(77535)
    print(output_sw.decode('utf-8'))

    time.sleep(2)
    print("Connecting to Next Device.\n\n")
    print(""" INFO: You need to enter a different username and password for the
            NX-Extreme Wireless Controller
            \n""")
    username2 = input("What is your username : ")
    password2 = getpass.getpass(prompt="Enter your password?: ")
    print("\nINFO: You are connecting to ", ip3, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip3, port=22, username=username2,
                         password=password2,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_nx = pre_ssh_conn.invoke_shell()
    banner_output3 = ssh_conn_sw.recv(89935)

    ssh_conn_nx.send("show global device-list | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nshow wireless ap on LS01005\n R")
    time.sleep(3)
    ssh_conn_nx.send("\nshow wireless client on LS01005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption status | i 1005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption offline | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nexit\n")
    time.sleep(1)

    output_nx = ssh_conn_sw.recv(89935)
    print(output_nx.decode('utf-8'))


    lg = "C:/Users/" + username + "/Desktop/[3]post-check-" + username + "-" + store_number + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
    print("\nLog file Created: " + lg)
    time.sleep(5)


elif device_type == "4":
    print("\n")
    store_number = input("INFO: Enter the store number: ")
    ip1 = input("INFO: ENCS-vEdge-VNF: Enter the IP:  ")
    ip2 = input("INFO: Cisco XXXX Switch: Enter The IP:  ")
    ip3 = input("INFO: NX-Extreme Wireless Controller: Enter the IP: ")
    username = input("What is your username: ")
    password = getpass.getpass(prompt="Enter your password?: ")


    print("\nINFO: You are connecting to ", ip1, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output4 = ssh_conn.recv(65535)


    ssh_conn.send("show control connections\n")
    time.sleep(1)
    ssh_conn.send("show bfd sessions \n")
    time.sleep(1)
    ssh_conn.send("show app-route stats local-color mpls |tab\n")
    time.sleep(1)
    ssh_conn.send("show app-route stats local-color green |tab\n")
    time.sleep(1)
    ssh_conn.send("show policy from-vsmart\n")
    time.sleep(1)
    ssh_conn.send("show cdp neighbors\n")
    time.sleep(1)
    ssh_conn.send("show arp vpn 2\n")
    time.sleep(1)
    ssh_conn.send("\nexit\n")
    time.sleep(1)

    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))
    print("\n\n")


    time.sleep(2)
    print("Connecting to Next Device.")
    print("\nINFO: You are connecting to ", ip2, "\n")
    time.sleep(1)
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip2, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output0 = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output_sw = ssh_conn_sw.recv(77535)
    print(output_sw.decode('utf-8'))


    time.sleep(2)
    print("Connecting to Next Device.\n\n")
    print(""" INFO: You need to enter a different username and password for the
                NX-Extreme Wireless Controller
                \n""")
    username2 = input("What is your username : ")
    password2 = getpass.getpass(prompt="Enter your password?: ")
    print("\nINFO: You are connecting to ", ip3, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip3, port=22, username=username2,
                         password=password2,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_nx = pre_ssh_conn.invoke_shell()
    banner_output41 = ssh_conn_sw.recv(89935)

    ssh_conn_nx.send("show global device-list | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nshow wireless ap on LS01005\n R")
    time.sleep(3)
    ssh_conn_nx.send("\nshow wireless client on LS01005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption status | i 1005\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption offline | i 1005\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nexit\n")
    time.sleep(1)

    output_nx = ssh_conn_sw.recv(89935)
    print(output_nx.decode('utf-8'))


    lg = "C:/Users/" + username + "/Desktop/[4]post-check-" + username + "-" + store_number + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
    print("\nLog file Created: " + lg)
    time.sleep(5)



elif device_type == "5":
    print("\n PRE: XXX Check \n")
    store_number = input("INFO: Enter the store number: ")
    ip1 = input("INFO: Cisco XXX Router: Enter the IP:  ")
    ip2 = input("INFO: Cisco XXX Switch: Enter The IP:  ")
    ip3 = input("INFO: Wireless Controller: Enter the IP: ")
    username = input("What is your username: ")
    password = getpass.getpass(prompt="Enter your password?: ")


    print("\nINFO: You are connecting to ", ip1, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(99535)


    ssh_conn.send("show ip route eigrp \n")
    time.sleep(1)
    ssh_conn.send("\n show dmvpn \n")
    time.sleep(1)
    ssh_conn.send("\n show ip route ospf \n")
    time.sleep(2)
    ssh_conn.send("\n ping repeat 100 source Loopback0 size 1024 \n")
    time.sleep(1)
    ssh_conn.send(" ping repeat 100 source Loopback0 size 1024 \n")
    time.sleep(1)
    ssh_conn.send(" show ip route eigrp \n")
    time.sleep(1)
    ssh_conn.send(" show dmvpn \n")
    time.sleep(1)
    ssh_conn.send(" show run int di0 \n")
    time.sleep(1)
    ssh_conn.send(" show ip int brief | show cdp nei detail | show int desc \n")
    time.sleep(1)
    ssh_conn.send("show ip arp \n")
    time.sleep(1)
    ssh_conn.send("\n exit \n")
    time.sleep(1)

    output_lr = ssh_conn.recv(99535)
    print(output_lr.decode('utf-8'))
    print("\n\n")


    time.sleep(2)
    print("\nINFO: Connecting to Next Device.")
    print("\nINFO: You are connecting to ", ip2, "\n")
    time.sleep(1)
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip2, port=22, username=username,
                         password=password,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_sw = pre_ssh_conn.invoke_shell()
    banner_output2 = ssh_conn_sw.recv(77535)

    ssh_conn_sw.send("show cdp neighbors\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow mac address-table\n")
    time.sleep(3)
    ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow ver | i bin\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow switch\n")
    time.sleep(5)
    ssh_conn_sw.send("\nshow logging\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
    time.sleep(1)
    ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
    time.sleep(1)
    ssh_conn_sw.send("\nexit\n")
    time.sleep(1)

    output_sw = ssh_conn_sw.recv(77535)
    print(output_sw.decode('utf-8'))


    time.sleep(2)
    print("Connecting to Next Device.\n\n")
    XXX_store = input("INFO:  Enter in the XXXX number (Only enter what goes into XXXX) : ")
    print("""\n INFO: You need to enter a different username and password for the
    NX-Extreme Wireless Controller
    \n""")
    username2 = input("What is your username : ")
    password2 = getpass.getpass(prompt="Enter your password?: ")
    print("\nINFO: You are connecting to ", ip3, "\n")

    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip3, port=22, username=username2,
                         password=password2,
                         look_for_keys=False, allow_agent=False)

    ssh_conn_nx = pre_ssh_conn.invoke_shell()
    banner_output3 = ssh_conn_sw.recv(89935)

    ssh_conn_nx.send("show global device-list | i XXX" + XXX_store + "\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nshow wireless ap on XXX" + XXX_store + "\n R")
    time.sleep(3)
    ssh_conn_nx.send("\nshow wireless client on XXX" + XXX_store + "\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption status | i XXX" + XXX_store + "\n R")
    time.sleep(1)
    ssh_conn_nx.send("\nshow adoption offline | i XXX" + XXX_store + "\n R")
    time.sleep(5)
    ssh_conn_nx.send("\nexit\n")
    time.sleep(1)

    output_nx = ssh_conn_sw.recv(89935)
    print(output_nx.decode('utf-8'))


    lg = "C:/Users/" + username + "/Desktop/[5]pre-check-" + username + "-" + ip1 + ".log"
    logfile = open(lg, "wb")
    logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
    print("\nLog file Created: " + lg)
    time.sleep(5)

# XXX CHECK XXX check

elif device_type == "6":
        print("\n POST: XXX Check \n")
        store_number = input("INFO: Enter the store number: ")
        ip1 = input("INFO: Cisco XXX Router: Enter the IP:  ")
        ip2 = input("INFO: Cisco XXX Switch: Enter The IP:  ")
        ip3 = input("INFO: NX-Extreme Wireless Controller: Enter the IP: ")
        username = input("What is your username: ")
        password = getpass.getpass(prompt="Enter your password?: ")


        print("\nINFO: You are connecting to ", ip1, "\n")

        pre_ssh_conn = paramiko.SSHClient()
        pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pre_ssh_conn.connect(ip1, port=22, username=username,
                             password=password,
                             look_for_keys=False, allow_agent=False)

        ssh_conn = pre_ssh_conn.invoke_shell()
        banner_output = ssh_conn.recv(99535)


        ssh_conn.send("show ip route eigrp \n")
        time.sleep(1)
        ssh_conn.send("\n show dmvpn \n")
        time.sleep(1)
        ssh_conn.send("\n show ip route ospf \n")
        time.sleep(2)
        ssh_conn.send("\n ping XXXXXXXXXXX repeat 100 source Loopback0 size 1024 \n")
        time.sleep(1)
        ssh_conn.send(" ping XXXXXXXXXX repeat 100 source Loopback0 size 1024 \n")
        time.sleep(1)
        ssh_conn.send(" show ip route eigrp \n")
        time.sleep(1)
        ssh_conn.send(" show dmvpn \n")
        time.sleep(1)
        ssh_conn.send(" show run int di0 \n")
        time.sleep(1)
        ssh_conn.send(" show ip int brief | show cdp nei detail | show int desc \n")
        time.sleep(1)
        ssh_conn.send("show ip arp \n")
        time.sleep(1)
        ssh_conn.send("\n exit \n")
        time.sleep(1)

        output_lr = ssh_conn.recv(99535)
        print(output_lr.decode('utf-8'))
        print("\n\n")


        time.sleep(2)
        print("\nINFO: Connecting to Next Device.")
        print("\nINFO: You are connecting to ", ip2, "\n")
        time.sleep(1)
        pre_ssh_conn = paramiko.SSHClient()
        pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pre_ssh_conn.connect(ip2, port=22, username=username,
                             password=password,
                             look_for_keys=False, allow_agent=False)

        ssh_conn_sw = pre_ssh_conn.invoke_shell()
        banner_output2 = ssh_conn_sw.recv(77535)

        ssh_conn_sw.send("show cdp neighbors\n")
        time.sleep(5)
        ssh_conn_sw.send("\nshow mac address-table\n")
        time.sleep(3)
        ssh_conn_sw.send("\nshow int desc | i up / show int desc | i down\n")
        time.sleep(1)
        ssh_conn_sw.send("\nshow ver | i bin\n")
        time.sleep(1)
        ssh_conn_sw.send("\nshow switch\n")
        time.sleep(5)
        ssh_conn_sw.send("\nshow logging\n")
        time.sleep(1)
        ssh_conn_sw.send("\nshow spanning-tree blockedports\n")
        time.sleep(1)
        ssh_conn_sw.send("\nshow interfaces status err-disabled\n")
        time.sleep(1)
        ssh_conn_sw.send("\nexit\n")
        time.sleep(1)

        output_sw = ssh_conn_sw.recv(77535)
        print(output_sw.decode('utf-8'))


        time.sleep(2)
        print("Connecting to Next Device. [XXX]\n\n")
        XXX_store = input("INFO:  Enter in the XXXXXXX number (Only enter what goes into XXXX) : ")
        print("""\n INFO: You need to enter a different username and password for the
        NX-Extreme Wireless Controller
        \n""")
        username2 = input("What is your username : ")
        password2 = getpass.getpass(prompt="Enter your password?: ")
        print("\nINFO: You are connecting to ", ip3, "\n")

        pre_ssh_conn = paramiko.SSHClient()
        pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pre_ssh_conn.connect(ip3, port=22, username=username2,
                             password=password2,
                             look_for_keys=False, allow_agent=False)

        ssh_conn_nx = pre_ssh_conn.invoke_shell()
        banner_output3 = ssh_conn_sw.recv(89935)

        ssh_conn_nx.send("show global device-list | i XXX" + XXX_store + "\n R")
        time.sleep(5)
        ssh_conn_nx.send("\nshow wireless ap on XXX" + XXX_store + "\n R")
        time.sleep(3)
        ssh_conn_nx.send("\nshow wireless client on XXX" + XXX_store + "\n R")
        time.sleep(1)
        ssh_conn_nx.send("\nshow adoption status | i XXX" + XXX_store + "\n R")
        time.sleep(1)
        ssh_conn_nx.send("\nshow adoption offline | i XXX" + XXX_store + "\n R")
        time.sleep(5)
        ssh_conn_nx.send("\nexit\n")
        time.sleep(1)

        output_nx = ssh_conn_sw.recv(89935)
        print(output_nx.decode('utf-8'))


        lg = "C:/Users/" + username + "/Desktop/[6]post-check-" + username + "-" + ip1 + ".log"
        logfile = open(lg, "wb")
        logfile.write(output_lr + "\n\n".encode('ascii') + output_sw + "\n\n".encode('ascii') + output_nx)
        print("\nLog file Created: " + lg)
        time.sleep(5)



elif device_type == "7":
    print("\n")
    print("************************************")
    print("*****                          *****")
    print("*****   Comparision Checker    *****")
    print("*****    Of Two Configs        *****")
    print("****                           *****")
    print("************************************")
    print("\n")
    print('\nWARNING: Discrepancies found:')


    def open_file_and_return_list(file_path):
        list = []
        with open(file_path, 'r') as f:
            line = f.readline()
            while line:
                list.append(line)
                line = f.readline()
        return list


    def clean_new_line(list):
        for i in range(len(list)):
            if "\n" in list[i]:
                list[i] = list[i].replace("\n", "")
        return list


    if __name__ == "__main__":
        s1 = input("INFO: Select the first file to compare:  ")
        s2 = input("INFO: Select the second file to compare: ")
        list1 = open_file_and_return_list(s1)
        list2 = open_file_and_return_list(s2)
        maxl = max(len(list1), len(list2))
        list1 += [''] * (maxl - len(list1))
        list2 += [''] * (maxl - len(list2))
        diff = []
        diff_file = input("\nINFO: Select what to name the difference(s) : ")
        open(diff_file, 'w').close()

        for iline, (l1, l2) in enumerate(zip(list1, list2)):
            if l1 != l2:
                print(iline, l1, l2)
                print(iline, l1, l2, file=open(diff_file, 'a'))
