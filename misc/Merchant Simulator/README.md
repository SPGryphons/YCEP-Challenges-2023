Merchant Simulator
===

## Summary
* **Author:** Bryan Lim
* **Discord Tag:** JusCodin#3049
* **Category:** Misc
* **Difficulty:** Easy

## Solution
Just a simple challenge, meant to introduce people to netcat challenges.
This challenge is a two-parter, with the other part abusing a bug in the game that is technically also in this version.
~~Please accept this I made an entire game from scratch for this~~

1. Connect to the server using netcat, and enter username as `muffin`.
2. When the game starts, you gain access to a new option called `Set gold`.
3. Using that option, set the gold amount to `1000000` either by entering `1000000` or `a`
4. Select the `Retire` option, and you will get the flag

NOTE: Technically this challenge might be solvable by just playing the game normally,
but if they suffered through 500 full in-game weeks and get 1000000 gold, they deserve it.

## Flag
```
YCEP2023{I_L0V3_M0N3Y_S0_MUCH}
```