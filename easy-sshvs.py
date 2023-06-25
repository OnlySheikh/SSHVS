import os
import time

def print_with_delay(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

delay = 0.04
print_with_delay("Welcome to Easy SSHVS(SSH VPN Server) v1.0 | Only Sheikh", delay)

while True:
    print_with_delay("1- Setup SSH VPN Server.", delay)
    print_with_delay("2- Add new SSH VPN User.", delay)
    print_with_delay("3- Get users list.", delay)
    print_with_delay("4- Delete a SSH VPN user.", delay)
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

        print_with_delay("Done! Enjoy and Eshqohalll :D", delay)
        print_with_delay("Now you can connect to this VPN Server via SSH connection.", delay)
        print_with_delay("Android and iOS Connection: NapsternetV", delay)
        print_with_delay("Windows Connection: Bitvise", delay)

    elif itemNumber == 2:
            clear = "clear"
            os.system(clear)
            userName = input("Enter new username(text): ")
            addUSER = "useradd -m " + str(userName)
            os.system(addUSER)
            print_with_delay("Please choose a password for user: "+ str(userName), delay)
            changePassword = "passwd " + str(userName)
            os.system(changePassword)
            noshellUSER = "usermod -s /bin/false " + str(userName)
            os.system(noshellUSER)
        
    elif itemNumber == 3:
            clear = "clear"
            os.system(clear)
            print_with_delay("All OS Users List:", delay)
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
