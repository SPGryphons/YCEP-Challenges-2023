# you can change the input into your final answer
a1 = input("What was the web password used?   : ").lower().encode() 
a2 = input("What was the cookie given?        : ").lower().encode() 
a3 = input("What was the payload encoded with?: ").lower().encode() 
a4 = input("What was the user's name?         : ").lower().encode() 
a5 = input("What was the file accessed?       : ").lower().encode() 
a6 = input("What was the file password used?  : ").lower().encode() 
a7 = input("What was the content of the file? : ").lower().encode() 
# do not change anything else in this program
buffer = a1+a2+a3+a4+a5+a6+a7

from hashlib import md5, sha1 
flag = 'YCEP2023{<replaceme>}'

if md5(buffer).hexdigest() != '':
    print("[-] Something somewhere isn't right")
else:
    print(f"[+] Congratulations!! {flag.replace('<replaceme>',sha1(buffer).hexdigest())}")