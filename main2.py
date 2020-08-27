import paramiko
import time
import re

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

#cat of old hostname
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



#sed old BU code for new in hostname 
sedofhostname = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /etc/hostname""" % locals(), """%(password)s""" % locals()]
for sed in sedofhostname:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhostname = channel.recv(9999) #read in
    print(newhostname.decode('utf-8'))
    time.sleep(0.1)


#sed old BU code for new in hosts
sedofhosts = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /etc/hosts""" % locals(), """%(password)s""" % locals()]
for sed in sedofhosts:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhosts = channel.recv(9999) #read in
    print(newhostname.decode('utf-8'))
    time.sleep(0.1)


#cat of hosts
catofhosts = ["""cat /etc/hosts"""]
for cat in catofhosts:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    catofthehostname = channel.recv(9999) #read in
    stringofcatofthehostname = (catofthehostname.decode('utf-8'))
    print(stringofcatofthehostname)       #raw output z cat hosts


#cat of new hostname
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
sliceofstringofmatches1 = stringofmatches[51:-2]
print ('Hostname of the server is : ' + sliceofstringofmatches1)

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


#old hostname z ktoreho potrebujem vytiahnut skratku kvoli repu
#input retch907-es4003
pattern3 = re.compile(r'.....+?(?=-)')
matches3 = pattern3.search(sliceofstringofmatches)
stringofmatches3 = str(matches3)
sliceofstringofmatches3 = stringofmatches3[41:-2]
#print ('Repo is : ' + sliceofstringofmatches3) #output ch907







#sed old BU code for new in hostname 
sedofhostname = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /root/config/%(sliceofstringofmatches3)s""" % locals(), """%(passwordrepo)s""" % locals()]   
for sed in sedofhostname:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhostname = channel.recv(9999) #read in
    print(newhostname.decode('utf-8'))
    time.sleep(0.1)







#reboot systemu ak potvrdim yes, ak nie tak loopback
while True:
    print('Do you want to reboot this machine? [Y/N]')
    rebootinput = input()
    if rebootinput == 'Y' or rebootinput == 'y' or rebootinput == 'yes':
        reboot = ["""sudo reboot""", """%(password)s""" % locals()]         
        for reb in reboot:
            channel.send(reb + "\n")
            while not channel.recv_ready(): #Wait for the server to read and respond
                time.sleep(0.1)
            time.sleep(0.1) #wait enough for writing to (hopefully) be finished
            rebooting = channel.recv(9999) #read in
            print(rebooting.decode('utf-8'))
            time.sleep(0.1)

    elif rebootinput == 'N' or rebootinput == 'n' or rebootinput == 'no':
        print ('System wont reboot, please do it on your own to apply all the changes')
        time.sleep(5)
        break
    else:
        print('WRONG INPUT, Please type Y/N | y/n | yes/no')
        time.sleep(2)

#zavre shh channel
channel.close()

