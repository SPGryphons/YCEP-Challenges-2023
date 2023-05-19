# you can change the input into your final answer
a1 = input("What was the web password used?   : ")
a2 = input("What was the cookie given?        : ")
a3 = input("What was the payload encoded with?: ")
a4 = input("What was the user's name?         : ")
a5 = input("What was the file first accessed? : ")
a6 = input("What was the file password used?  : ")
a7 = input("What was the content of the img?  : ")
# do not change anything else in this program
buffer = (a1+a2+a3+a4+a5+a6+a7).lower().encode()

from hashlib import md5, sha1 
flag = 'YCEP2023{<replaceme>}'
if md5(buffer).hexdigest() != '3d5307b14acde65fb67d7ad7538ef3b7':
    print("[-] Something somewhere isn't right")
else:
    print(f"[+] Congratulations!! {flag.replace('<replaceme>',sha1(buffer).hexdigest())}")