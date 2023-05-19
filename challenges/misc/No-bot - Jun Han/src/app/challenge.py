import time 
import hashlib
from base64 import b64encode, b64decode

def challenge():
    o = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
    y = hashlib.sha256(o.encode()).hexdigest()
    epoch = b64encode(f'{int(time.time())}'.encode())
    x = ord(o[-2]) >> 3
    m = b64decode(epoch)
    t = int(m.decode('utf-8'))
    f = t << x
    r = hashlib.sha512(str(f).encode()).hexdigest()  + y
    k = hashlib.sha256(r.encode()).hexdigest()

    print(f) # encrypted challenge payload
    return k[56:]