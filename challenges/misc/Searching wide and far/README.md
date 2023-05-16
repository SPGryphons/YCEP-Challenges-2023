Searching wide and far
===

## Summary
- Author:	Gabriel
- Discord Tag: 	duckupus#6365
- Category: 	Misc
- Difficulty:	Medium

## Solution
1. Vulnerability is in `strstr` function, where the `hackstack` and `needle` are flipped.
2. Connect to netcat instance. Enter the string `FractionMonkeyPeachesRandomAldenpneumonoultramicroscopicsilicovolcanoconiosissyzygybloviatecalligraphy` 64 times to get the flag

## Flag
```
YCEP2023{h4ys7aCk_1n_The_n3edl3_1nd33d}
```
