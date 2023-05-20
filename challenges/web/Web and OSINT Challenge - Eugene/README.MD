Web and OSINT 

Summary
Author: Eugene

Discord Tag: Testing8191#4985

Category: Web/OSINT

Difficulty: Medium

Solution
1. To find second piece, go to 'Blog' in nav bar and click any one of the posts
2. Notice the post ids in blog are '2' and '3' only. The '1' is missing
3. Change the url to use /blog_1
4. Use dev tools and find the script that interactively load content in each post
5. Copy the id and follow the hint to visit the URL
6. The instructions and second piece is provided (Piece 2: DISM_DCDF_ROCKS)
7. Go back to blog, go to first blog post displayed
8. In the fake terminal, there is a user account with password exposed. Remember that
9. Go back to login page and type them in. It says the password length must be min 8, but ours 7
10. We can complete the form by typing any 8 char or more pass, the URL will have additional parameters
11. Change the 'pass' section to what we found earlier (test123)
12. The admin panel will appear. We can reset the 'admin' account password to anything >= 8 chars (or we have to pass in the password parameters again)
13. Use this new password to login to 'admin' account
14. Get piece (Piece 1: WOW_OMG)
15. Go back to blog, go to second blog post displayed
16. Solve the questions using OSINT, you will get (Piece 3: FELIDAE_MOLLY_FERAL)
17. Go back to home page, type the pieces together in the instructions, get (WOW_OMGDISM_DCDF_ROCKSFELIDAE_MOLLY_FERAL)
18. Submit the form and get flag

Flag
YCEP2023{DISM_DCDF_FOREVER}
