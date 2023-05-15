# Calligraphy Lesson
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Forensics
* **Difficulty:** Medium

## Solution
- Use `file` command to find the file type for `character.png`.
- Open `character.png` on a hex editor and add the PNG file headers to the first few bytes of the file.
- Open the file in an image viewer.
- After research, the character is a Japanese kanji character named "taito" (たいと).
- This is the password for the zip file (which also can be cracked with john).
- The `nothing.txt` file hints that the flag is hidden inside the image and rotate the bytes 84 times (the number strokes of the character). The location of the flag is in `0x0000840` line of the hex editor. The flag should be visible when opened in a hex editor again.

## Flag
```
YCEP2023{k4nJ1_15_L1k3_cH1n353_8U7_No7_ch1n353_lOl}
```