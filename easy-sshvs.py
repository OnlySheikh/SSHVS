import os

print("Welcome to Easy SSHVS(SSH VPN Server) v1.0 | Only Sheikh")

while True:
    print("1- Setup SSH VPN Server.")
    print("2- Add new SSH VPN User.")
    print("3- Get users list.")
    print("4- Delete a SSH VPN user.")
    itemNumber = input("Choose one of the items(number): ")

    itemNumber = int(itemNumber)
    if itemNumber == 1:
        clear = "clear"
        os.system(clear)
        sshPORT = input("Choose a new SSH Port(number): ")

        with open('/etc/ssh/sshd_config') as f:
            lines = f.read()

        lines = lines.replace('#AllowAgentForwarding yes', 'AllowAgentForwarding yes')
        lines = lines.replace('#AllowTcpForwarding yes','AllowTcpForwarding yes')
        lines = lines.replace('#TCPKeepAlive yes', 'TCPKeepAlive yes')
        lines = lines.replace("#Port 22", "Port "+str(sshPORT))
        lines = lines.replace("Port 22", "Port "+str(sshPORT))

        saveSSHD = open("/etc/ssh/sshd_config", "w")
        saveSSHD.write(lines)
        saveSSHD.close()

        restartSSHD = 'systemctl restart sshd'
        os.system(restartSSHD)

        print("Done! Enjoy and Eshqohalll :D")
        print("Now you can connect to this VPN Server via SSH connection.")
        print("Android and iOS Connection: NapsternetV")
        print("Windows Connection: Bitvise")

    elif itemNumber == 2:
            clear = "clear"
            os.system(clear)
            userName = input("Enter new username(text): ")
            addUSER = "useradd -m " + str(userName)
            os.system(addUSER)
            print("Please choose a password for user: "+ str(userName))
            changePassword = "passwd " + str(userName)
            os.system(changePassword)
            noshellUSER = "usermod -s /bin/false " + str(userName)
            os.system(noshellUSER)
        
    elif itemNumber == 3:
            clear = "clear"
            os.system(clear)
            print("All OS Users List:")
            listUSER = "cut -d: -f1 /etc/passwd"
            os.system(listUSER)

    elif itemNumber == 4:
            clear = "clear"
            os.system(clear)
            delUsername = input("Enter a username for delete(text): ")
            killall = "killall -TERM -u " + delUsername
            os.system(killall)
            delUSER = "userdel -r " + delUsername
            os.system(delUSER)
