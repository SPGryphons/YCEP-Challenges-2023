with open("enc.txt", "r") as f:
    cipher = f.read().strip()

for letter in cipher.split("_"):
    if letter:
        print(chr(int(letter)), end="")