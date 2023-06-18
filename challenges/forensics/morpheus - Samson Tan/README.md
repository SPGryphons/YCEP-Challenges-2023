Morpheus
===

## Summary
* **Author:** Samson Tan
* **Discord Tag:** eclip#6943
* **Category:** Forensics
* **Difficulty:** Medium

## Description
This your last chance. After this, there is no turning back.<br>
You take the blue pill, the story ends. You wake up in your bed and believe whatever you want to.<br>
You take the RED PIL, you stay in Wonderland, and I show you how deep the rabbit hole goes.<br>
Remember, all I'm offering is the truth. Nothing more.

## Hints
1. Why is pill spelled like that? Is this guy dyslexic?
2. Focus on the color of the pill that Neo took.
3. Unleash the hidden potential of x and y by fusing their existence into a singular enigmatic entity.

## Solution
1. Install and import <b>Python Image Library (PIL)</b> package, use the <b>Image</b> module
    ``` python
    from PIL import Image
    ```

2. Scan through every pixel of the image
    ``` python
    asciiArr = []

    image = Image.open(r"challenge.png")
    pixel = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1])
    ```

3. Find the coordinates of all pixels with an RGB value of (255,0,0) and add the <b>x</b> and <b>y</b> values together
    ``` python
    if (pixel[x,y] == (255,0,0)):
            asciiCode = x + y
            asciiArr.append(asciiCode)
    ```

4. Convert the ASCII code to text
    ``` python
    flag = ''
    for item in asciiArr:
        flag += chr(item)

    print(flag)
    ```

## Flag
```
YCEP2023{7H15_R48817_H0L3_G035_D33P}
```