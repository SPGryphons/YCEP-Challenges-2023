import time
import hashlib
from pwn import *

io = remote('172.17.0.2', 8000)
# io = process('src/main.py')

def calculate_hash():
    '''
    Derived from Epoch value and the initial hash IV
    '''
    filler = io.recvuntil(b'Challenge (provide last 8 hash values): \n')
    challenge = io.recvuntil(b'No-bot >')
    print(challenge)
    value = challenge.decode('utf-8').split('\n')
    # [NOTE] the source code uses base64 for obfuscation.
    # Nothing fancy happens to the epoch value
    left_bit_shift = int(value[0].strip())        # epoch << 7 (bit shift by 7)


    initial_iv = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
    initial_hash = hashlib.sha256(initial_iv.encode()).hexdigest()
    x = ord(initial_iv[-2]) >> 3         # 56 >> 3 = 7
    combined_hash = hashlib.sha512(str(left_bit_shift).encode()).hexdigest() + initial_hash
    final_hash = hashlib.sha256(combined_hash.encode()).hexdigest()
    last_eight_values = final_hash[56:]
    print("(+) Solve script starting...")
    print(f'left_bit: {left_bit_shift}')
    print(f'initial_hash: {initial_hash}')
    print(f'combined_hash: {combined_hash}')
    print(f'final_hash: {final_hash}')
    print(f'last_eight_values: {last_eight_values}')
    io.sendline(f'{last_eight_values}'.encode())
    

for i in range(100000):
    if i % 100 == 0 or i == 0:
        calculate_hash()

    # filler = io.recvuntil(b'Q')
    question = io.recvuntil(b'>')
    print(question)
    values = question.decode('utf-8').split()

    print(values[0])
    qn_value = values[1:6]
    qn = ' '.join(qn_value)
    answer = int(eval(qn))

    print(answer)
    io.sendline(f'{answer}'.encode())

flag = io.recvall()
print(flag.decode('utf-8'))

io.interactive()
