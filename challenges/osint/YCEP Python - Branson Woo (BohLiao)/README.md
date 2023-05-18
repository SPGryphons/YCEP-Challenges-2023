Wall Troll
===

## Summary

   - Author: Branson Woo Wung Lai
   - Discord Tag: BohLiao#7322
   - Category: OSINT / Insanity check
   - Difficulty: Medium

## Solution
Option A - For they, were codeless...:

1. Download [grepWin](https://tools.stefankueng.com/grepWin.html), a simple search and replace tool which can use regular expressions to do its job.
2. Opening grepWin, open the folder which contains 'Trolled.txt'.
3. Since the hacker only used 0 to 9 as a troll, have greWin search for these numbers one by one and replace them with nothing. (Ensure that Trolled.txt is one of the txt files that contains these numbers at the bottom of grepWin.)
4. The only thing left in the txt file should be the flag's contents.
5. Party!

Option B - Automation rocks!:
1. Studying through the file, one realises that it is completely filled with evenly spaced numbers from 0 - 9. (If they really looked, they'd realise there was 1,000,000 numbers. :D)
2. Now that you know the differences, create a python file to solve search through the entire file for unique characters and insert it into a new text file. OR Search the Internet to learn how to have Python actually do it.
3. Party!

## Flag

YCEP2023{Are_U_Is_Insane_Bro?}

## Extra

Produced with problem.py
Solved with sol.py
