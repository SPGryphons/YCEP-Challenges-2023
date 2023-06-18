# Pokemon GO!
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Reverse Engineering
* **Difficulty:** Hard

## Solution
1. This program is coded in Go. In the shell, run the program to play the Pokemon game.
2. If the user understands the logic behind Go, they should be able to find a secret function and backdoors that prints a flag with the correct inputs after winning the Pokemon game.
3. The user can then reverse engineer the function to find two clues which leads them to find to an obfuscated function.
4. To call the obfuscated argument, the user needs to enter "backdoor2" to call the function.
5. Deciphering all the obfuscated code in the `cHJpbnRYT1JGbGFn()` function, user understands that the function takes in a filename as a command-line argument.
6. After running the program again with the file "something.txt" as a command-line argument, the user will get a lot of Es once they win and enter "backdoor2" as the secret phrase.
7. The Es is a Cetacean cipher. The user can decipher the cipher with Cyberchef or other online tools to get the flag.

## Flag
```
YCEP2023{1+pl4y+P0K3m0N+90+3V3ryd4y}
```