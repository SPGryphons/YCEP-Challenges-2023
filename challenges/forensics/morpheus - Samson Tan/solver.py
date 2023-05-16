from PIL import Image

# Solving for flag ################################################
asciiArr = []

image = Image.open(r"challenge.png")
pixel = image.load()
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if (pixel[x,y] == (255,0,0)):
            asciiCode = x + y
            asciiArr.append(asciiCode)

flag = ''
for item in asciiArr:
    flag += chr(item)

print(flag)