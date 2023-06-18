Ascii71
===

## Summary
- Author: Lucius Chee Zihan
- Discord Tag: lcz5#3392
- Category: Cryptography
- Difficulty: Hard

## Solution
Ascii71 splits plaintext into blocks of 3 bytes (pads ends with \x00 if less than 3), concatenates their binary representations and then divides the result by 71 repeatedly. The remainder of each operation shall be the index of the alphabet (e.g. 0 -> "3"), or represented by ASCII code `<remainder>` + 51.
This is very similar to how Ascii85 does its encoding.
A script is highly recommended for this challenge.

1. From the encoded text, split it into blocks of 4.
2. In each block, take the ascii char code of the first character and minus 51. This value shall be `num`.
3. For every character, perform step 3, 4, and 5.
4. Take the ascii char code of the character and minus 51.
5. Multiply `num` by 71 and add the result of step 3, storing it in `num`.

6. After iterating through all characters, convert `num` into a binary representation and split it into 3 equal parts.
7. For each split part, add to the decoded string, the ASCII representation of the binary number.
8. After iterating through everything, we shall get the flag. Ignore the `\x00` characters for the purpose of this challenge.

A decoding script is shown below, in Python:
```python
import math
def from_ascii71(encoded):
    blocks = split_blocks(4, encoded)
    decoded = ""
    
    for block in blocks:
        
        num = ord(block[0]) - 51
        
        for c in block[1:]:
            """
            *71 + remainder
            """
            char = ord(c) - 51
            num = num * 71 + char
                block_bin_str = format(num, "08b").zfill(24)

        splits = []
        if len(block_bin_str) != 24:
            print("len is not 24! ")
            return
        splits.append(block_bin_str[0:8])
        splits.append(block_bin_str[8:16])
        splits.append(block_bin_str[16:])

        
        for bl in splits:
            block = "".join(bl)
            decoded += chr(int(block, 2))
    return decoded

# Split blocks function
def split_blocks(size, data):
    blocks = []
    iters = math.ceil(len(data) / size)
    for i in range(iters):
        index = i*size
        block = []
        for x in range(index, index + size):
            if x < len(data):
                block.append(data[x])
            else:
                block.append("\0")
        blocks.append(block)
    return blocks
                
print(from_ascii71(input("Enter encoded text here: ")))
```

## Flag
```
YCEP2023{3nC0din9_1S_noT_encrYPT10n}
```

## Additional notes
Here is the encoding script:
```python
import math
def split_blocks(size, data):
    blocks = []
    iters = math.ceil(len(data) / size)
    for i in range(iters):
        index = i*size
        block = []
        for x in range(index, index + size):
            if x < len(data):
                block.append(data[x])
            else:
                block.append("\0")
        blocks.append(block)
    return blocks


def to_ascii71(data):
    blocks = split_blocks(3, data)
    encoded = ""
    for block in blocks:
        block_bin_str = ""
        for char in block:
            block_bin_str += format(ord(char), "08b")
        block_bin = int(block_bin_str, 2)
        
        group = ""
        res = block_bin
        for i in range(4):
            remainder = res % 71
            res = int(res / 71)
            character = remainder + 51            
            group += chr(character)
        encoded += "".join(reversed(group)) # Because when decoding, they read the other way around. This is implemented even in Ascii85.
    return encoded

print(to_ascii71(input("enter flag here: ")))
```
