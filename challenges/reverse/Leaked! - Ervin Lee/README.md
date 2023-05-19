# Leaked!
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Reverse Engineering
* **Difficulty:** Hard

## Solution
1. The participant is given an Assembly file called `leak.s` and a binary file called `scraps.bin`.
2. The participant is required to reverse engineer the Assembly file to find the flag.
3. The assembly file is a script that performs a shift cipher on each flag character with a random shift value and then writes it to the binary file.
4. Understanding the logic of the Assembly file, the participant should recreate it by coding a script to read the binary file and perform the reverse shift cipher on each character.

## Flag
```
YCEP2023{4223m8ly_c0D3_15_pr377y_C4NC3r_N9l}
```