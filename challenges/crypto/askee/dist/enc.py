with open('flag.txt', 'r') as f:
    flag = f.read().strip()

ascii_flag = ''
for char in flag:
    ascii_flag += str(ord(char)) + '_'

with open('enc.txt', 'w') as f:
    f.write(ascii_flag)