from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# PLEASE DO NOT TAMPER WITH THE ORIGINAL encrypted_flag.txt, encrypted_aes_key.txt, and iv.txt FILES!!!
# If you want to test this script, make a copy and modify the directories accordingly.

flag = "flag{this_is_a_flag}"
iv = get_random_bytes(AES.block_size)

# Import Public Key
file_in = open("2Keys\code\key2.pem", "rb")
public_key = RSA.import_key(file_in.read())
print(public_key)
file_in.close()

# Import Private Key
file_in = open("2Keys\code\key1.pem", "rb")
private_key = RSA.import_key(file_in.read())
print(private_key)
file_in.close()

# Oops, my computer crashed and I lot a lot of progress on my code. Can you help me recover the flag?