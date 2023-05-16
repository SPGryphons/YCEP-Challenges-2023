EXploring Is Fun
===

## Summary
* **Author:** Samson Tan
* **Discord Tag:** eclip#6943
* **Category:** Forensics
* **Difficulty:** Easy

## Description
I need the exact coordinates of where this photo was taken.<br>
Find it one way or another, detective.

Flag format: `YCEP2023{xx deg xx' xx.xx" N, xx deg xx' xx.xx" E}`<br>
(Ignore leading zeroes)

## Solution
1. Use exiftool to view the metadata of the image.

2. Copy the coordinates in the EXIF data into the format of the flag.

## Flag
```
YCEP2023{43 deg 28' 6.39" N, 11 deg 52' 53.45" E}
```