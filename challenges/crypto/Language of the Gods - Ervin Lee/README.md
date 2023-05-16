Language of the Gods
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Cryptography
* **Difficulty:** Medium

## Solution
- The flag is an abbreviated form of a LaTex expression
- Refer to https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols for a list of LaTex symbols
- Manually translate the symbols into LaTex encoding and abbreviate it into the flag by taking the first letter after the backslashes
- Use ROT to decipher the plaintext into the flag.

## Flag
```
YCEP2023{latex_is_fun}
```