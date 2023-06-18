# HACKME (Boot-2-Root)

## Summary

- **Author:** Lennon Chee
- **Discord Tag:** Tanjiro Kamado#5928
- **Category:** Pwn 
- **Difficulty:** Medium

## Solution

use NMAP to scan the virtual machine to view the open ports. try ftp anonymous login. 

Get keys.txt and new.txt

Use from Base64 to decode the text.

find the “anomaly” (hex input) and decrypt with AES.

Key and IV is in the txt file.

## Flag

```
YCEP2023{This_is_the_flag}
```

## Download Link
https://ichatspedu-my.sharepoint.com/:u:/g/personal/lennonchee_22_ichat_sp_edu_sg/EVtv23RhqnpGr59NHW6rLAMBIvSttXHNJp7JOalOyBw0dw?e=wq9zoa