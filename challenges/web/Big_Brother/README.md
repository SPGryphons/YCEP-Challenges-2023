Big Brother
===

## Summary
* **Author:** Samson Tan
* **Discord Tag:** eclip#6943
* **Category:** Web
* **Difficulty:** Hard

## Description
Everywhere you go, every person you talk to, Big Brother is watching.<br>
I found the webpage where he stores his core files.<br>
If you can escape him and get the flag there, I can shut him down for good.

## Setup
Run ```./build.sh``` in the service directory.<br>
Port is 50982

## Solution
1. In the main.js file, all the way at the bottom, there is a commented out Base64 string declared.
    ``` javascript
    let him_cook = "YnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgZnVuY3Rpb24oKSB7CiAgICBmZXRjaCgiaHR0cDovL2xvY2FsaG9zdDo1MDk4Mi95b3V3aWxsbmV2ZXJicnV0ZWZvcmNldGhpc2FwaSIpCiAgICAudGhlbihyZXNwb25zZSA9PiByZXNwb25zZS5qc29uKCkpCiAgICAudGhlbihkYXRhID0+IHsKICAgICAgY29uc29sZS5sb2coZGF0YSk7CiAgICB9KQogICAgLmNhdGNoKGVycm9yID0+IHsKICAgICAgY29uc29sZS5lcnJvcignRXJyb3I6JywgZXJyb3IpOwogICAgfSk7Cn0pOw=="
    ```
2. Decoding this will give a function that handles the event of the 'Get Flag' button being clicked.
    ``` javascript
    button.addEventListener('click', function() {
        fetch("http://localhost:50982/youwillneverbruteforcethisapi")
        .then(response => response.json())
        .then(data => {
        console.log(data);
        })
        .catch(error => {
        console.error('Error:', error);
        });
    });
    ```

3. Browsing to the URL will display a page saying that the flag has been hidden by Big Brother.<br>
    ![alt text](https://gcdnb.pbrd.co/images/wBKFobTdqImw.png?o=1)

4. The participant has to view the response headers when querying the endpoint to get the flag.<br>
    ![alt text](https://gcdnb.pbrd.co/images/sqiZ4sD85LI5.png?o=1)

5. The flag is encoded in Base85. Decode it and you will get the flag.<br>
    ![alt text](https://gcdnb.pbrd.co/images/3oOhx7skQIwO.png?o=1)

## Flag
```
YCEP2023{n3Xt_T1M3_w0n7_b3_e4sY_l177l3_0n3}
```