# Happy Hotel
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Pwn
* **Difficulty:** Medium

## Solution
- Simple buffer overflow challenge
- Spam a bunch of letters to find the overflowing of letters in the output
- Manipulate the number of letters until the user output after the input is blank and control the output ending with H100 to get the desired user's room and the flag

## Flag
```
YCEP2023{H4z81n_h073l}
```
