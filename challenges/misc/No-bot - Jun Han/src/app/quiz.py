import random

def questions():
    c = 87654321
    operation = ['*', '+', '-', '/']
    l = []

    for i in range(100000):
        x = random.randint(1000000, 9000000)
        y = random.randint(1000000, 9000000)
        s = operation[random.randint(0,3)]
        answer = int(eval(f"({x}{s}{y})*{c}"))
        o = f"Q{i+1}: ({x} {s} {y}) * {c} = ?"
        # print(o)
        l.append((o, answer))
    
    return l

def win():
    with open('../flag.txt') as f:
        print(f.read())
