diffie heavenman
===

## Summary
* **Author:** Andre
* **Discord Tag:** dre#0001
* **Category:** Crypto
* **Difficulty:** Medium (difficulty can be increased by changing password to the value of secret key and adding intercept.txt with g^b mod p)

## Solution
1. As our goal is to find the secret key of alice, one of the algorithms we can use is the pohlig-hellman algorithm in order to get the value of a through g^a mod p.
2. Sage math's discrete_log function implements the pohlig hellman algorithm, so we can write a simple script using sage to find alice secret key.
3. Unzip the folder with the secret key of alice (18381761546331816928970576078022427)

## Flag
```
YCEP2023{d1Ff1e_P0ll4rd_p0hL1g}
```