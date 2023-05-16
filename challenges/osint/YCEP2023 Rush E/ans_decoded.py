# fake_flag = "YCEP2023{abcdefghijklmnopqrstuvwxyz}"
flag = "YCEP2023{Ru$h_E!}"
to_decode = [221, 59, 46, 185, 235, 228, 235, 93, 541, 3, 269, 19, 1874, 49, 46, 142, 424]
msg = [str(ord(i)) for i in flag]
print(msg)

def encode():
    # ================= DO NOT EDIT THIS ====================
    import decimal as dc
    # set the precision
    dc.getcontext().prec = 6001
    factorial = 1
    euler = 2
    for x in range(2, 150):
        factorial *= x
        euler += dc.Decimal(str(1.0))/dc.Decimal(str(factorial))
    # print( "6000 digit of Eulers number:")
    # print(euler)
    # ================= DO NOT EDIT THIS ====================
    string = ""
    for i in range(6000):
        digit = int(euler)
        string += str(digit)
        euler -= digit
        euler *= 10
    return [string.find(letter) for letter in msg]
# print(encode())

def decode(decode_msg):
    import decimal as dc
    # set the precision
    dc.getcontext().prec = 6001
    factorial = 1
    euler = 2
    for x in range(2, 150):
        factorial *= x
        euler += dc.Decimal(str(1.0))/dc.Decimal(str(factorial))

    string = ""
    for i in range(6000):
        digit = int(euler)
        string += str(digit)
        euler -= digit
        euler *= 10

    x = [string[int(i):int(i)+2] for i in decode_msg]
    y = [string[int(i):int(i)+3] for i in decode_msg]
    total = ""
    for a,b in zip(x,y):
        if int(b) < 127:
            total += chr(int(b))
        else:
            total += chr(int(a))
    return total

print(decode(to_decode))
