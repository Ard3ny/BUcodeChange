import paramiko
import time
import re


host = '192.168.100.20'
username = 'filip'
password = 'aaa'



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



#vytiahne hostname zo stringu s catom a vypise cisty hostname 
pattern = re.compile(r'hostname\s\s.+?(?=\s)')
matches = pattern.search(stringofhostnametobechanged)
stringofmatches = str(matches)
sliceofstringofmatches = stringofmatches[51:-2]
print ('Hostname of the server is : ' + sliceofstringofmatches)



channel.close()

