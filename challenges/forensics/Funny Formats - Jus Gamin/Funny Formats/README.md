Funny Formats
===

## Summary
* **Author:** Bryan Lim
* **Discord Tag:** JusCodin#3049
* **Category:** Forensics
* **Difficulty:** Easy

## Solution
We have 4 files in the zip file, chall_1.txt, chall_2.zip, chall_3, and chall_4.

1. chall_1.txt is actually a zip file so just rename it to chall_1.zip and extract it.
2. chall_2.zip is actually a 7z file so just rename it to chall_2.7z and extract it. The flag fragment is in flag.txt, but its actually an image file so just rename it to flag.jpg and open it.
3. chall_3.zip can be unzipped normally and has a file called README.md but its actually a word document so just rename it to README.docx and open it. The flag fragment is inside it.
4. chall_4.zip was zipped using WinRAR so just rename it to chall_4.rar and extract it. Then open `file` with WinRAR 5 times to get the flag fragment.

## Flag
```
YCEP2023{F0rm4tt1nG_1s_4n_4rt}
```