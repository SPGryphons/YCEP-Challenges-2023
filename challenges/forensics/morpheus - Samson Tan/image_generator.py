from PIL import Image
import random

# Create challenge.png from an image ##############################
image = Image.open(r"images/morpheus.png")
pixel = image.load()
with open('coordinates.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    x,y = line.replace('\n','').split(',')
    pixel[int(x),int(y)] = (255,0,0)

# Generate red herring
for i in range(50):
    randx = random.randint(150, 251)
    randy = random.randint(1, 100)
    if pixel[randx, randy] != (255,0,0):
        pixel[randx,randy] = (0,0,255)

image.save('challenge.png')
