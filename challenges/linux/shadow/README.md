Shadow 2
===

## Summary
* **Author:** Zavier Lee
* **Discord Tag:** gatari#0000
* **Category:** Linux
* **Difficulty:** Medium

## Solution
1. `cat /etc/shadow` and `cat /etc/passwd` to get the hashes and usernames, see that there is a user called `pwn_me`.
2. Use `john` to crack the hashes, instructions can be found below.
3. Run `su pwn_me` to login as `pwn_me`.
4. `cat /home/pwn_me/flag.txt` to get the flag.

## Flag
```
YCEP2023{how_CouLD_yOU_CR@cK_my_P45$WorD}
```

## Instructions for `john`
1. Save the contents of `/etc/shadow` to a file called `shadow.txt`.
2. Save the contents of `/etc/passwd` to a file called `passwd.txt`.
3. Run `unshadow passwd.txt shadow.txt > unshadowed.txt`.
4. `john --wordlist=/usr/share/wordlists/rockyou.txt --format=crypt unshadowed.txt`
5. Wait for it to finish, then run `john --show unshadowed.txt` to see the cracked passwords.

lucky13          (pwn_me)
