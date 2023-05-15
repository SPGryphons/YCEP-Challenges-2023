# Suspicious Blog
This blog seems to be hiding something from us. Can you uncover it?

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** Web
+ **Difficulty:** Medium

## Solution
1. Inspect the source code of the page. Take note of the weird filenames in the `src` attributes.
2. According to the number in the `alt` attributes, rearrange and combine the corresponding filenames into one string (excluding the extension). 
3. For the 4th filename, it suggests the 4th part of the string is hidden somewhere else. Look at the Javascript code of `/static/button.js` and the 4th part of the string is commented in the code.
4. Convert the whole string from Base64 and obtain the name of a secret page. Add `/s3cr3t-p4gE-wottt` to the back of the original URL and browse to the secret page.
5. Change the `cookie` value from `none` to `Chocolate Chip`, and refresh the page to obtain the flag. 

## Flag
```
YCEP2023{5U5P1C10U5_BL0G_3XP053D}
```