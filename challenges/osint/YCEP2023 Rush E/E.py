fake_flag = "YCEP2023{abcdefghijklmnopqrstuvwxyz}"
# flag = [221, 59, 46, 185, 235, 228, 235, 93, 541, 3, 269, 19, 1874, 49, 46, 142, 424]
msg = [str(ord(i)) for i in fake_flag]

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