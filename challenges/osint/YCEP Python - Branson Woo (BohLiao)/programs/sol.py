unique = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

file = open('Trollr.txt', 'r')
 
while 1:
     
    # read by character
    char = file.read(1)         
    if not char:
        break
    w = open('flag.txt', "a")
    if char not in unique:
        w.write(char)
 
file.close()