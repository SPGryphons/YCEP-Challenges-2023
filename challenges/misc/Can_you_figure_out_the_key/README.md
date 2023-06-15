# Can you figure out the key?

Description -   nc chal.dismgryphons.com 7000

Download File - server.py

Author - Rean Schwarzer#9086

Dockerize - Dockerfile and app.py

Flag - CTF101{R3ver5e_1s_Fun}

# Explanation - Run the exploit.py

**server.py** <br>
The server.py script is to sign and verify messages. It uses a simple keyed-hash message authentication algorithm based on the md5 hash function.<br>
The options provided by the server.py script are:

1) Sign messages: It allows the user to enter a message and generates a signed message by appending the message with a key and computing the hash using the sign() function.

2) Verify messages: It allows the user to enter a signed message and verifies if the message is signed by the correct key using the verify() function. If the verification is successful, it prints "Message verified!" and if correct key and (PASSPHRASE = "Better than HMAC!"), it will display a flag from a flag.txt file.

**exploit.py** <br>
The additional options provided by the exploit.py script are:

3) Input signed messages to find key: It allows the user to input a signed message and iterates through all possible keys to find a key that verifies the given signed message using the verify() function. If a key is found, it is printed as the output.

4) Input key to find signed passphrase: It allows the user to input a key and generates a signed passphrase by appending a predefined passphrase with the input key and computing the hash using the sign() function. The signed passphrase is then printed as the output.
