from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Import Private Key
file_in = open(".\key1.pem", "rb")
private_key = RSA.import_key(file_in.read())
print(private_key)
file_in.close()

# Import Encrypted AES Key
file_in = open(".\encrypted_aes_key.txt", "rb")
encrypted_aes_key = file_in.read()
file_in.close()

# Import IV
file_in = open(".\iv.txt", "rb")
iv = file_in.read()
file_in.close()

# Import Encrypted Flag
file_in = open(".\encrypted_flag.txt", "rb")
ciphertext = file_in.read()
file_in.close()

# Decrypt AES Key with Private Key
cipher = PKCS1_OAEP.new(private_key)
session_aes_key = cipher.decrypt(encrypted_aes_key)

# Decrypt Flag with AES Key
cipher = AES.new(session_aes_key, AES.MODE_CBC, iv)
decrypt = cipher.decrypt(ciphertext)
decrypt = unpad(decrypt, 16)
decrypted = decrypt.decode()

print("Decrypted Flag: ", decrypted)

# YCEP2023{R1Ve5T-5H4m1r-4DLEm4n}