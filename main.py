import paramiko


host = "10.60.215.15"
port = 22
username = "wincor\filip.zverec.adm"
password = "Wiab105kosice"

command = "ll"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)