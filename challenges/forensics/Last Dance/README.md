# Last Dance
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Forensics
* **Difficulty:** Medium

## Solution
- The two halves of a PNG image are encoded and stored in binary files (First half is in `last.bin` and the second half in `dance.bin`)
- The PNG image is a Blue Screen of Death where there is a modified QR code that will redirect you to a Google Drive link to download a WAV file.
- The flag file is hidden inside the WAV file.
- Using password cracking tools such as John the Ripper, we can extract the flag from the audio file using `steghide extract`.
- Flag is written to a file called `flag.txt`.

## Flag
```
YCEP2023{R4150N-d37r3}
```