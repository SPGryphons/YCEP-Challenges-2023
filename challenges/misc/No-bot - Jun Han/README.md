# No-Bot

## Summary
- **Author:** Ng Jun Han
- **Discord Tag:** GoldenStone02#9852
- **Category:** Reverse Engineering/Misc
- **Difficulty:** Hard

## Solution
1. Reverse engineering the captcha that was created in `No-bot\src\app\challenge.py`. (Epoch value with hash and bitwise operations)
2. Write a function to solve the captcha challenge
```python
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
    left_bit_shift = int(value[0].strip())

    initial_iv = 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'
    initial_hash = hashlib.sha256(initial_iv.encode()).hexdigest()
    x = ord(initial_iv[-2]) >> 3         # 56 >> 3 = 7
    combined_hash = hashlib.sha512(str(left_bit_shift).encode()).hexdigest() + initial_hash
    final_hash = hashlib.sha256(combined_hash.encode()).hexdigest()
    last_eight_values = final_hash[56:]
    io.sendline(f'{last_eight_values}'.encode())
```
3. Then create a script to solve the randomized math problems that are prompted.
```python
from pwn import *

for i in range(100000):
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
```
4. Add a conditional check for every 100 question to calculate the hash
```python
if i % 100 == 0 or i == 0:
    calculate_hash()
```
5. Put these components together and run the script. (Refer to [solve.py](/No-bot/solve.py) for the solution script)

## Flag
```
YCEP2023{5cr1ptNg_4nD_cRyp70_l3g3ND}
```

## Additional Notes
- Replace the flag.txt with the actual flag
- Use `sudo docker build -t nobot .` & `sudo docker run -it -d --publish 8000:8000 nobot` to build and deploy the image