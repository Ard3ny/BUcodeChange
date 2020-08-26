import paramiko
import time
import re


#host = '192.168.100.20'
#username = 'filip'
#password = 'aaa'

print ('IP address of the server: ')
host = input()
print ('Username: ')
username = input()
print ('Pasword: ')
password = input()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
channel = client.invoke_shell()

# clear welcome message and send newline
time.sleep(1) 
channel.recv(9999)
channel.send("\n")
time.sleep(1)


catofhostname = ["""cat /etc/hostname"""]
for cat in catofhostname:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    hostnameToBeChanged = channel.recv(9999) #read in
    #print(hostnameToBeChanged.decode('utf-8'))
    stringofhostnametobechanged = (hostnameToBeChanged.decode('utf-8'))
    #print(repr(stringofhostnametobechanged))   #raw verzia pre dalsie spracovanie
    #print(hostnameToBeChanged.decode('utf-8'))  #prehladnejsia verzia s medzerami pre konzolu
    time.sleep(0.1)


#vytiahne hostname zo stringu s catom a vypise cisty hostname 
pattern = re.compile(r'hostname\s\s.+?(?=\s)')
matches = pattern.search(stringofhostnametobechanged)
stringofmatches = str(matches)
sliceofstringofmatches = stringofmatches[52:-2]
print ('Hostname of the server is : ' + sliceofstringofmatches)


#input pre stary a novy bu code pomoocu ktoreho sa vykona sed
print ('Type old BU code')
oldbucode = input()
print ('Type new BU code')
newbucode = input()


#Scrubnuty napad asi
#zmena hostname podla stareho hostname na novy hostname balbla zatial
# sedofhostname = ["""sudo sed -i 's/%(sliceofstringofmatches)s/filip/g' /etc/hostname""" % locals(), """aaa""", """cat /etc/hostname"""]
# for sed in sedofhostname:
#     channel.send(sed + "\n")
#     while not channel.recv_ready(): #Wait for the server to read and respond
#         time.sleep(0.1)
#     time.sleep(0.1) #wait enough for writing to (hopefully) be finished
#     newhostname = channel.recv(9999) #read in
#     print(newhostname.decode('utf-8'))
#     time.sleep(0.1)



#sed old BU code for new 
sedofhostname = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /etc/hostname""" % locals(), """aaa"""]
for sed in sedofhostname:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhostname = channel.recv(9999) #read in
    print(newhostname.decode('utf-8'))
    time.sleep(0.1)

catofhostname = ["""cat /etc/hostname"""]
for cat in catofhostname:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    hostnameToBeChanged = channel.recv(9999) #read in
    #print(hostnameToBeChanged.decode('utf-8'))
    stringofhostnametobechanged = (hostnameToBeChanged.decode('utf-8'))
    #print(repr(stringofhostnametobechanged))   #raw verzia pre dalsie spracovanie
    #print(hostnameToBeChanged.decode('utf-8'))  #prehladnejsia verzia s medzerami pre konzolu
    time.sleep(0.1)




#vytiahne hostname zo stringu s catom a vypise cisty hostname podla paternu pomocou RE
pattern = re.compile(r'hostname\s\s.+?(?=\s)')
matches = pattern.search(stringofhostnametobechanged)
stringofmatches = str(matches)
sliceofstringofmatches = stringofmatches[51:-2]
print ('Hostname of the server is : ' + sliceofstringofmatches)



#ip adresa servera
ipofserver = ["""ip a"""]
for ip in ipofserver:
    channel.send(ip + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    ipaddress = channel.recv(9999) #read in
    stringofipaddress = (ipaddress.decode('utf-8'))
    #print(stringofipaddress)       #raw IP output z ip a
    time.sleep(0.1)

#vytiahne ip adressu zo stringu podla paternu pomocou RE
pattern2 = re.compile(r'inet.+?(?=brd)')
matches2 = pattern2.search(stringofipaddress)
stringofmatches2 = str(matches2)
sliceofstringofmatches2 = stringofmatches2[46:]
print ('IP of the server is : ' + sliceofstringofmatches2)


#reboot systemu ak potvrdim yes 
print('Do you want to reboot this machine? [Y/N]')
rebootinput = input()
if rebootinput == 'Y' or rebootinput == 'y' or rebootinput == 'yes':
    reboot = ["""pwd"""]         #pwd na test
    for rebooting in reboot:
        channel.send(rebooting + "\n")
        while not channel.recv_ready(): #Wait for the server to read and respond
            time.sleep(0.1)
        time.sleep(0.1) #wait enough for writing to (hopefully) be finished
        rebooting = channel.recv(9999) #read in
        stringofrebooting = (rebooting.decode('utf-8'))
        print(stringofrebooting)       #raw output z rebootu
        time.sleep(0.1)

elif rebootinput == 'N' or rebootinput == 'n' or rebootinput == 'no':
    print ('Ok, system wont reboot, please do it on your own to apply all the changes')

else:
    print('System wont reboot, please input Y/N')



#zavre shh channel
channel.close()

