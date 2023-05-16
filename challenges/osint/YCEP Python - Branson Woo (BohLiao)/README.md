Wall Troll
===

## Summary

   - Author: Branson Woo Wung Lai
   - Discord Tag: BohLiao#7322
   - Category: OSINT / Insanity check
   - Difficulty: Medium

## Solution

1. Download [grepWin](https://tools.stefankueng.com/grepWin.html), a simple search and replace tool which can use regular expressions to do its job.
2. Opening grepWin, open the folder which contains 'Trolled.txt'.
3. Since the hacker only used 0 to 9 as a troll, have greWin search for these numbers one by one and replace them with nothing. (Ensure that Trolled.txt is one of the txt files that contains these numbers at the bottom of grepWin.)
4. The only thing left in the txt file should be the flag's contents.
5. Party!

## Flag

YCEP2023{Are_U_Is_Insane_Bro?}

## Extra

Produced with the script YCEP.py