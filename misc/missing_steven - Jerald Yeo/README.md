# Missing Steven
A man, Steven, has gone missing and it's your job to find him! A note was left behind.

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** Misc (OSINT, Crypto)
+ **Difficulty:** Medium

## Solution
1. In `note.txt`, the first letter of every sentence spells out **"YOUTUBE"**. Search up **"steven.tanROCKZ145"** on Youtube.

2. In the "whee whew" video, at around 1:45, take note of the first portion of an encrypted flag that appears briefly. 

3. In the "roblox sad story" video, at around 0:58, the username **"steventantantan_tan"** appears, with a sentence above it: 

    > follow me and i will buy a **Steam** game for you less than $25!

    Search up the username on Steam. Also, take note of the comment under the video:

    > who is **Vigenere**?

4. In the Steam user's profile picture, the second portion of the encrypted flag is visible.

5. Back in `note.txt`, the following text provides the key to decrypt the flag:

    > The key is **determination**.

6. Use any tool (such as Cyberchef) to decrypt the flag using the Vigenere cipher and obtain the flag.

## Flag
```
YCEP2023{ST3V3N_T4N_1S_S4F3}
```

## Account Credentials
**Youtube (Gmail account)**
+ Email: steventanzzzzzzz@gmail.com
+ Password: sT3v3nTANN123

**Steam Account**
+ Username: steventantantan_tan
+ Password: sT3v3nTANN123
