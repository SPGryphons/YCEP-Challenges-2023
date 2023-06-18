# Robot Conversation
In a world where robots coexist with humans, there are rumours of the robots planning to erase the human population and dominate the world. Can you investigate this exchange between 2 robots suspected of conspiring against humans?

## Summary
+ **Author:** Jerald Yeo
+ **Discord Tag:** maximus#4723
+ **Category:** Crypto
+ **Difficulty:** Easy

## Solution
1. Convert the whole conversation (only the 1's and 0's) from Binary to Text (ASCII/UTF-8) to get the following:

    > Initialising connection with #2719...  
      Connection established!  
      Hey, I need the password to the zip files of the secret plans.
    > 
    > I can't tell you right now. The humans could be listening to us.
    > 
    > No, they can't. Humans don't speak binary language, only we do!
    > 
    > Hmm.. you're right. Alright, here's the encrypted password: **SWYJ2023{7B3_F4H6O463_0Z_W0GJO73L5}**  
    > You'll have to decrypt it by yourself to get the original password.
    > 
    > Thanks! An extra layer of encryption, huh?
    > 
    > Just for good measure. Anyways, remember that we'll be meeting Boss in **6** days to present our findings on human behaviour.
    > 
    > Yup, see you then!  
      Ending connection... Goodbye. 

2. The flag `SWYJ2023{7B3_F4H6O463_0Z_W0GJO73L5}` is encrypted using Caesar cipher. Decrypt it using the shift length of `6` and obtain the flag.

## Flag
```
YCEP2023{7H3_L4N6U463_0F_C0MPU73R5}
```