# Shadow

## Description
Shadow have crack a very important key, now is your job to infiltrate and find the data <br>
Location: chal.gryphons.sg <br>
Gate: 7003 <br>
Strategy: Secure Shell <br>
Author - Rean Schwarzer#9086 <br>
download file - cracked_shadow.txt

## Solution
ssh user@chal.gryphons.sg -p 7003 <br>
Once ssh into the docker, the user will have rbash (restricted shell) to find the flag in /home/user directory. User must use ls -a to find the real hidden flag file (/home/user/.flag.txt).

## Flag
YCEP2023{L1nux_Wi11_4lw4y5_B3_W1th_Y0u}
