import os
import socket

print("Welcome to Easy SSHVS(SSH VPN Server) v1.0 | Only Sheikh")
sshPORT = input("Choose a new SSH Port(number): ")

with open('/etc/ssh/sshd_config') as f:
    lines = f.read()

lines = lines.replace('#AllowAgentForwarding yes','AllowAgentForwarding yes')
lines = lines.replace('#AllowTcpForwarding yes','AllowTcpForwarding yes')
lines = lines.replace('#TCPKeepAlive yes','TCPKeepAlive yes')
lines = lines.replace('#Port 22','Port '+str(sshPORT))

saveSSHD = open("/etc/ssh/sshd_config","w")
saveSSHD.write(lines)
saveSSHD.close()

restartSSHD = 'systemctl restart sshd'
os.system(restartSSHD)

print("Done! Enjoy and Eshqohalll :D")
print("Now you can connect to this VPN Server via SSH connection.")
print("Android Connection: NapsternetV")
print("Windows Connection: Bitvise")





