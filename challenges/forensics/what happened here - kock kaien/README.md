what happened here
===

Something tragic happened to our shared linux server. Investigate and note your findings at autocomputer.py to get the flag.

## Summary
* **Author:** Koh Kai En
* **Discord Tag:** thereconman#2688
* **Category:** Forensics
* **Difficulty:** Hard

## Solution
1. Open up the pcapng file in wireshark
2. Find the password used to login (goblin)
3. Find the token given after giving goblin (7E24253C39078C42652BF9E5921901C2)
4. Find the payload, and understand its hexadecimal encoding
5. Find the whoami command to find the username (rogue)
6. File accessed was hotimages.zip
7. Find 7z command with -p (opensesame)
8. Final image was encoded with hexadecimal (h0tp1cs!)
9. Compute all the items with sha1 and get the flag

## Flag
```
YCEP2023{d5648f47aa7b566e6447bf1987b8677c4995af29}
```