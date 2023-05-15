Hidden Gateway
===

## Summary
* **Author:** Darius Chew
* **Discord Tag:** dc.darius#8903
* **Category:** Web
* **Difficulty:** Medium

## Solution
1. Base64 encode the string 'opensesame' to get 'b3BlbnNlc2FtZQ=='.
2. Append this as a 'secret_key' parameter to the URL, e.g., http://localhost:1337/?secret_key=b3BlbnNlc2FtZQ==.
3. Visit this URL, and the flag 'YCEP2023{h1dd3n_g4t3w4y}' will be revealed on the page.

## Flag
```
YCEP2023{h1dd3n_g4t3w4y}
```