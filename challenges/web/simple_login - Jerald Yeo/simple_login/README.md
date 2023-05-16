# Simple Login
Login and find the flag.

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** Web
+ **Difficulty:** Easy

## Solution
1. Log in with any credentials. It shows that you have the role of `guest`.
2. Go back to the login page and inspect elements to see the hidden form input `role`, with the value of `guest`.
3. Change from `guest` to `admin` and login again to obtain the flag.


## Flag
```
YCEP2023{5N34KY_H1DD3N_1NPU7}
```