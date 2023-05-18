# Uncovering the Secret
Zachary Lim Yi Xuan is suspected of hiding a secret piece of information. Please try to find out what he's hiding.

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** OSINT
+ **Difficulty:** Medium

## Solution
1. Search for `Zachary Lim Yi Xuan` on LinkedIn and view his posts.
2. In the following post:

    > Gave the Linux penguin a makeover. It looks much better !

    There is a GitHub link partially visible in the Messages window in the screenshot: `https://github.com/zachdoes...`. Search for a user in GitHub whose username starts with this. The 2nd half of the username is also partially visible below to help in finding the correct user.

3. After locating GitHub user `zachdoescodinthings`, view his repositories. In the repository `coolAPI`, view `req.py`. Scroll to the bottom of the file to see his Twitter username (Line 62).

    > ...  
    > ...  
    > \# Get user's profile information  
    > username = '**allziswell_**'  
    > user = api.get_user(username)  
    > ...  
    > ...  

4. Search for the user `@allziswell_` on Twitter and view his posts. Scroll down to see his older posts, where one contains a Base64 encoded text:

    > WUNFUDIwMjN7UzM0UkNIMU42X0ZSME1fNENDMFVON19UMF80Q0MwVU43fQ==

    Decode it to obtain the flag.

## Flag
```
YCEP2023{S34RCH1N6_FR0M_4CC0UN7_T0_4CC0UN7}
```

## Account Credentials
**Gmail Account**
+ Email: z4ch4ryl1my1xu4n@gmail.com
+ Password: yti8758%TU76hkjh

**LinkedIn** (_Sign in with Google_)
+ Email: z4ch4ryl1my1xu4n@gmail.com
+ Password: yti8758%TU76hkjh

**GitHub**
+ Username: zachdoescodinthings
+ Password: yti8758%TU76hkjh

**Twitter** (_Sign in with Google_)
+ Email: z4ch4ryl1my1xu4n@gmail.com
+ Password: yti8758%TU76hkjh
