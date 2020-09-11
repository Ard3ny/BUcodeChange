import paramiko
import time
import re


print ('IP address of the server: ')
host = input()
# print ('Username: ')
# username = input()
# print ('Pasword: ')
# password = input()

#host = '192.168.100.8'
username = 'cio_ad_s'
password = 'nohpCCM2016,'

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
        time.sleep(0.5)
    time.sleep(0.5) #wait enough for writing to (hopefully) be finished
    hostnameToBeChanged = channel.recv(9999) #read in
    time.sleep(0.5) 
    
    #print(repr(stringofhostnametobechanged))   #raw verzia pre dalsie spracovanie
    #print(hostnameToBeChanged.decode('utf-8'))  #prehladnejsia verzia s medzerami pre konzolu
    stringofhostnametobechanged = (hostnameToBeChanged.decode('utf-8'))
    time.sleep(0.5)

#vytiahne hostname zo stringu s catom a vypise cisty hostname 
pattern = re.compile(r'hostname\s\s.+?(?=\s)')
matches = pattern.search(stringofhostnametobechanged)
stringofmatches = str(matches)
sliceofstringofmatches = stringofmatches[52:-2]
print ('---------------------------------------------------------------------')
print ('Hostname of the server is : ' + sliceofstringofmatches)
print ('---------------------------------------------------------------------') 

#input pre stary a novy bu code pomoocu ktoreho sa vykona sed
print ('Type old BU code [xxx] x=only numbers')
oldbucode = input()
print ('Type new BU code [xxx] x=only numbers')
newbucode = input()



#sed old BU code for new in hostname 
sedofhostname = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /etc/hostname""" % locals(), """%(password)s""" % locals()]
for sed in sedofhostname:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhostname = channel.recv(9999) #read in
    #print ('---------------------------------------------------------------------')
    #print(newhostname.decode('utf-8'))
    #print ('---------------------------------------------------------------------')
    time.sleep(0.1)


#sed old BU code for new in hosts
sedofhosts = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /etc/hosts""" % locals(), """%(password)s""" % locals()]
for sed in sedofhosts:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhosts = channel.recv(9999) #read in
    #print ('---------------------------------------------------------------------')
    #print(newhostname.decode('utf-8'))
    #print ('TOTO NECHAT2?')
    #print ('---------------------------------------------------------------------')
    time.sleep(0.1)


#cat of hosts
catofhosts = ["""cat /etc/hosts"""]
for cat in catofhosts:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.5)
    time.sleep(0.5) #wait enough for writing to (hopefully) be finished
    catofthehostname = channel.recv(9999) #read in
    stringofcatofthehostname = (catofthehostname.decode('utf-8'))
    print ('---------------------------------------------------------------------')
    print(stringofcatofthehostname)       #raw output z cat hosts
    print ('---------------------------------------------------------------------')


#cat of new hostname
catofhostname = ["""cat /etc/hostname"""]
for cat in catofhostname:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.5)
    time.sleep(0.5) #wait enough for writing to (hopefully) be finished
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
print ('---------------------------------------------------------------------')
print ('Hostname of the server is : ' + sliceofstringofmatches1)
print ('---------------------------------------------------------------------')

catofhostname = ["""cat /etc/hostname"""]
for cat in catofhostname:
    channel.send(cat + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.5)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    hostnameToBeChanged = channel.recv(9999) #read in
    #print(hostnameToBeChanged.decode('utf-8'))
    stringofhostnametobechanged = (hostnameToBeChanged.decode('utf-8'))
    #print(repr(stringofhostnametobechanged))   #raw verzia pre dalsie spracovanie
    #print(hostnameToBeChanged.decode('utf-8'))  #prehladnejsia verzia s medzerami pre konzolu
    time.sleep(0.5)



#ip adresa servera
ipofserver = ["""ip a"""]
for ip in ipofserver:
    channel.send(ip + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.5)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    ipaddress = channel.recv(9999) #read in
    stringofipaddress = (ipaddress.decode('utf-8'))
    #print(stringofipaddress)       #raw IP output z ip a
    time.sleep(0.5)

#vytiahne ip adressu zo stringu podla paternu pomocou RE
pattern2 = re.compile(r'inet.+?(?=brd)')
matches2 = pattern2.search(stringofipaddress)
stringofmatches2 = str(matches2)
sliceofstringofmatches2 = stringofmatches2[46:]
print ('---------------------------------------------------------------------')
print ('IP of the server is : ' + sliceofstringofmatches2)
print ('---------------------------------------------------------------------')

#------------------------------------------------------------------------------------------------------
#TRIETIA CAST KODU DOCASNE VLOZENA SEM KYM BUDE FUNKCNA


newilohostname = sliceofstringofmatches1 + '.wincor.ikea.com'  #output sliceofstringofmatches je retch666-es4003 a treba zmenit na retch666-es4003.wincor.ikea.com
#v sudo mode vojde do /tmp a echo configu vlozi do changehostanme.xml a cez hpconfg updatne ilo name

while True:
    print('Do you want to change ILO hostname of the machine? [Y/N]')
    ilonameyesno = input()
    if ilonameyesno == 'Y' or ilonameyesno == 'y' or ilonameyesno == 'yes':
        makefileandfillit = ["""sudo su -""", """%(password)s""" % locals(),  """cd /tmp""", """echo "<RIBCL VERSION="2.0">
  <LOGIN USER_LOGIN=\"admin\" PASSWORD=\"Password\">
    <SERVER_INFO MODE=\"write\">
 <SERVER_NAME value =\"%(newilohostname)s\"/>
    </SERVER_INFO>
  </LOGIN>
</RIBCL>" > changehostname.xml""" % locals(), """hponcfg -f changehostname.xml"""]
        for insert in makefileandfillit:
            channel.send(insert + "\n")
            while not channel.recv_ready(): #Wait for the server to read and respond
                time.sleep(0.5)
            time.sleep(0.1) #wait enough for writing to (hopefully) be finished
            newilohostname = channel.recv(9999) #read in
            print(newilohostname.decode('utf-8'))
            time.sleep(0.5)
        print ('---------------------------------------------------------------------')
        print ('ILO of the server was successfully changed')
        print ('---------------------------------------------------------------------')
        break
    elif ilonameyesno == 'N' or ilonameyesno == 'n' or ilonameyesno == 'no':
        print ('System wont change ILO hostname')
        time.sleep(2)
        break
    else:
        print('WRONG INPUT, Please type Y/N | y/n | yes/no')
        time.sleep(2)




#------------------------------------------------------------------------------------------------------

#reboot systemu ak potvrdim yes, ak nie tak loopback
while True:
    print('Do you want to reboot this machine? [Y/N]')
    rebootinput = input()
    if rebootinput == 'Y' or rebootinput == 'y' or rebootinput == 'yes':
        reboot = ["""sudo su -""", """%(password)s""" % locals(), """/sbin/reboot"""]         
        for reb in reboot:
            channel.send(reb + "\n")
            while not channel.recv_ready(): #Wait for the server to read and respond
                time.sleep(0.5)
        print ('System is rebooting')
        break
    elif rebootinput == 'N' or rebootinput == 'n' or rebootinput == 'no':
        print ('System wont reboot, please do it on your own to apply all the changes')
        time.sleep(2)
        break
    else:
        print('WRONG INPUT, Please type Y/N | y/n | yes/no')
        time.sleep(2)


#zavre shh channel
channel.close()





#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#DRUHA CAST KODU


while True:
    print('Do you want to update repo server with new BU code? [Y/N]')
    repochanges = input()
    if repochanges == 'Y' or repochanges == 'y' or repochanges == 'yes':


        hostrepo = 'deika9010is021p'
        usernamerepo = 'cio_ad_s'
        passwordrepo = 'TsimbCIO5!'
        # hostrepo = '192.168.100.8'
        # usernamerepo = 'root'
        print ('You will be logged in as ' + usernamerepo)
        # print ('Please enter the password of repo server: ')
        # passwordrepo = input()


        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostrepo, username=usernamerepo, password=passwordrepo)
        channel = client.invoke_shell()

        # clear welcome message and send newline
        time.sleep(1) 
        channel.recv(9999)
        channel.send("\n")
        time.sleep(1)

        #old hostname z ktoreho potrebujem vytiahnut skratku kvoli repu
        #input retch907-es4003
        pattern3 = re.compile(r'.....+?(?=-)')
        matches3 = pattern3.search(sliceofstringofmatches)
        stringofmatches3 = str(matches3)
        sliceofstringofmatches3 = stringofmatches3[41:-2]
        #print ('Repo is : ' + sliceofstringofmatches3) #output ch907
        sliceofhostnameshortcut = sliceofstringofmatches3[0:2] #output ch
        sliceofhostnameshortcutPLUSnewbucode = sliceofhostnameshortcut + newbucode #output ch+oldbucode




        #sed old BU code for new in hostname
        sedofhostname = ["""sudo su -""", """%(passwordrepo)s""" % locals(), """cd /root/config""",  """sed -i 's/%(oldbucode)s/%(newbucode)s/g' %(sliceofstringofmatches3)s""" % locals(), """mv %(sliceofstringofmatches3)s %(sliceofhostnameshortcutPLUSnewbucode)s""" % locals()]  
        for sed in sedofhostname:
            channel.send(sed + "\n")
            while not channel.recv_ready(): #Wait for the server to read and respond
                time.sleep(0.5)
            time.sleep(0.1) #wait enough for writing to (hopefully) be finished
            newhostname = channel.recv(9999) #read in
            print(newhostname.decode('utf-8'))
            time.sleep(0.5)


        #zavre shh channel
        channel.close()
        print ('----------------------------------------------------------------------------------------------------------------------')
        print ('Everthing inside of the ' + sliceofstringofmatches3 + ' has been successfully sed from ' + oldbucode + ' to ' + newbucode)
        print ('Repo server ' + sliceofstringofmatches3 + ' has been successfully changed to ' + sliceofhostnameshortcutPLUSnewbucode)
        print ('----------------------------------------------------------------------------------------------------------------------')
        time.sleep(20)
        break
    elif rebootinput == 'N' or rebootinput == 'n' or rebootinput == 'no':
        print ('No changes to the repo server will be made')
        time.sleep(5)
        break
    else:
        print('WRONG INPUT, Please type Y/N | y/n | yes/no')
        time.sleep(2)





