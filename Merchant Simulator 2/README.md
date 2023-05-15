Merchant Simulator 2
===

## Summary
* **Author:** Bryan Lim
* **Discord Tag:** JusCodin#3049
* **Category:** Misc
* **Difficulty:** Medium

## Solution
This game is based of an insanely old game called "Taipan!", where you sail your ship to different places and buy and sell stuff.
In both Taipan and this game, there is a bug with the money loaning system where it is possible to pay off more than you actually owe. This causes the amount you owe to be negative, and because of the absurdly high interest rate in this game, is a source of infinite money.

1. Connect to the server using netcat
2. When the game starts, go to the bank
3. Take out a loan of any amount
4. Pay off that loan with the `borrowed amount + 100` (Do not press "A" as that will only pay off what is owed)
5. Exit the bank and keep passing time until the owed amount is less than `-1000000` and press `Retire`

NOTE: If you find any of the ascii art in the `ads` folder potentially inappropriate do contact me and I'll change it to something else

## Flag
```
YCEP2023{N3G4T1V3_INT3RE5T_F0R_TH3_W1N}
```