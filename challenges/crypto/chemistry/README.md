chemistry
===
we used one chemical and one compound to dissolve the flag
find which combination we used to recover it

## Summary
- Author: Koh Kai En
- Discord Tag: thereconman#2688
- Category: Cryptography
- Difficulty: Hard

## Solution
1. Bruteforce the combination of chemicals and compounds (chemical_7 and compound_4)
2. XOR together with the enc flag to get original flag

## Flag
```
YCEP2023{x0R_oP3rAt10Ns_aR3_c0NFuS1nG}
```

Solve.py
```python

def xor(a:bytes,b:bytes):
    if len(a) == len(b):
        xored = []
        for i in range(len(a)):
            xored.append((a[i] ^ b[i]).to_bytes(1,'little'))
        return b''.join(xored)
    else:
        return None
    
flag = b'\xa0%\xb5[\xaa\xa2fN\x17\xed\x0c~\x01\xcfN\x10"th\xc1\xd5\xbb\x98\x9f\xbe\xe5xn\xba\xda\xbf\x17z?\x96\x04m\xb3'
chemical_1 = b"\x9fM'\xbf\x9dt\xc4\x02\xe2\x93yH\x03\xees\xf8{\x12o\x8a'\x04\xd9U\xb5\xb0\xb2L\t\xc9\xe8\x08\xc9\x97\x8cS\x1fm"
chemical_2 = b'\xa2\x03\x153\xa1\xec\xf4\xd7@Z %\xc4\xecI@C`\xa5\x06\x9d\xbdo\xdf\x8de,\x99\x82\xddt\x80\xdb\x06\xe6\xc3\xe3\x9a'
chemical_3 = b"\xbb\xff\x1d\x8c\xee\xc3\x11\x11\x81:o\xf2\x9e\xeb~evS\x08\x8de\xf2YJ\xc3i\x88AP&\x1f9'G\xee%\xd7\xb4"
chemical_4 = b'\x14\xe7Lv\x020H\xd9\xb6\x83mW`Q_;*\xa1I\xe3\x8dCu\xcaF}K\xc3\xb4\x87\x8b\x0f\r\x1aD\xae0\xbf'
chemical_5 = b'\xc4!\x95\x14\xc7%\xa5\x81T\x9fR\x98\x90\x0c\x84\xa8\xef\xda\xe5i(\xd2\xa1\x1d\xa3\xd0\xb1\xf8\xba.\xcfy\x1d\xc52\xbe\xda\xba'
chemical_6 = b'\xed\x81\xbc}\x9a\xa2\x1c\xa4\xda\x16Q{>\xf1A\x18z\x94U\x13h\xb6\x9e\n\x99\xca\x00\xf2mmz^\x02v\xe3\xc4\x1aq'
chemical_7 = b'r\x02q2\xc5=\t\x86\x99\xea\xcds\x19\xd5\xc11\xce\x8a\xc9\x9b\xb3}B\xbb\xc6an\xc8\x9b\x1d\xf2V\x8a\x98\xb0\xb6\x9aF'
compound_1 = xor(xor(chemical_1,chemical_5),chemical_3) 
compound_2 = xor(xor(compound_1,chemical_1),chemical_7) 
compound_3 = xor(chemical_4,chemical_6) 
compound_4 = xor(xor(xor(compound_2,chemical_3),compound_3),chemical_5) 
compound_5 = xor(chemical_2,chemical_7) 
compound_6 = xor(xor(compound_5,compound_3),chemical_6) 
compound_7 = xor(chemical_5,compound_4) 

l = [chemical_1,chemical_2,chemical_3,chemical_4,chemical_5,chemical_6,chemical_7]
y = [compound_1,compound_2,compound_3,compound_4,compound_5,compound_6,compound_7]

for i in range(len(l)):
    for j in range(len(y)):
        try:
            print(xor(flag,xor(l[i],y[j])).decode())
        except:
            continue

```
