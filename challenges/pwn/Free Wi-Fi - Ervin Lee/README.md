# Free Wi-Fi
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Pwn
* **Difficulty:** Hard

## Solution
- Solve script is in `solve.py`
- The verbose prompt is vulnerable to buffer overflow. Overwrite the verbose status variable to ON in order to get details of what is happening in the program
- The password prompt is also vulnerable to buffer overflow. Overwrite the password check variable to TRUE in order to bypass the password check
- Once connected to the Wi-Fi, notice that the program is still running. This is because the program is still running in the background. The program is vulnerable to format string attacks and the flag is stored in the stack. Use format string attacks to leak the flag from the stack. (`%x`)

## Flag
```
YCEP2023{pL345E_d0N7_c0NN3c7_70_574rBUcK5_w1F1}
```