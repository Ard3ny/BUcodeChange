import paramiko

print ('Zadaj hostname/IP servera')
host = input()
print ('Zadaj username')
username = input()
print ('Zadaj heslo')
password = input()
port = 22

command = "ll"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)