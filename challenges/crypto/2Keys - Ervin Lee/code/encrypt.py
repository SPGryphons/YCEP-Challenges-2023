from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

flag = "YCEP2023{R1Ve5T-5H4m1r-4DLEm4n}"
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

# Generate AES Key
session_aes_key = get_random_bytes(AES.block_size)
iv = get_random_bytes(AES.block_size)

# Encrypt AES Key with Public Key
cipher = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher.encrypt(session_aes_key)

# Encrypt Flag with AES Key
block_size = 16
cipher = AES.new(session_aes_key, AES.MODE_CBC, iv) # AES Cipher in CBC Mode
bytes = pad(flag.encode(), 16)
encrypted = cipher.encrypt(bytes)

print("Encrypted Flag: ", encrypted.hex())
print("Encrypted AES Key: ", encrypted_aes_key.hex())
print("IV: ", iv.hex())

# Write Encrypted Flag to File
file_out = open("2Keys\code\encrypted_flag.txt", "wb")
file_out.write(encrypted)
file_out.close()

# Write Encrypted AES Key to File
file_out = open("2Keys\code\encrypted_aes_key.txt", "wb")
file_out.write(encrypted_aes_key)
file_out.close()

# Write IV to File
file_out = open("2Keys\code\iv.txt", "wb")
file_out.write(iv)
file_out.close()