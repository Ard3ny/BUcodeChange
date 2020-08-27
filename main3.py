import paramiko
import time
import re
from main2 import oldbucode
from main2 import newbucode
from main2 import sliceofstringofmatches

host = '192.168.100.20'   	#repo server 
username = 'filip'  		#cio_ad_s
password = 'aaa'			#toto bude na input zadaj heslo 


# #ssh client 
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(host, username=username, password=password)
# channel = client.invoke_shell()


# # clear welcome message and send newline
# time.sleep(1) 
# channel.recv(9999)
# channel.send("\n")
# time.sleep(1)


#old hostname z ktoreho potrebujem vytiahnut skratku kvoli repu
#input retch907-es4003
pattern3 = re.compile(r'.....+?(?=-)')
matches3 = pattern3.search(sliceofstringofmatches)
stringofmatches3 = str(matches3)
sliceofstringofmatches3 = stringofmatches3[41:-2]
#print ('Repo is : ' + sliceofstringofmatches3) #output ch907



#sed old BU code for new in hostname 
sedofhostname = ["""sudo sed -i 's/%(oldbucode)s/%(newbucode)s/g' /root/config/%(sliceofstringofmatches3)s""" % locals(), """%(password)s""" % locals()]   
for sed in sedofhostname:
    channel.send(sed + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    newhostname = channel.recv(9999) #read in
    print(newhostname.decode('utf-8'))
    time.sleep(0.1)




 print ('toto znamena ze ide main3')
 time.sleep(10)