import sys
import time
from Crypto.Cipher import DES
from Crypto import Random
import os
# acquire parameters
iv = sys.argv[1]
key = sys.argv[2]
inputfile = sys.argv[3]
outputfile = sys.argv[4]
try:
    f1 = open(inputfile, 'r', encoding = "latin-1")
    f2 = open(outputfile, 'w', encoding = "latin-1")
except Exception as e:
    print(e)


#cbc_key = Random.get_random_bytes(8)

print('=' * 100)
print('Key used: ', [x for x in key])


#iv = Random.get_random_bytes(8)

print("IV used: ", [x for x in iv])
print('=' * 100)

try:
    des1 = DES.new(bytearray.fromhex(key), DES.MODE_CBC, bytearray.fromhex(iv))
    des2 = DES.new(bytearray.fromhex(key), DES.MODE_CBC, bytearray.fromhex(iv))
except Exception as e:
    print(e)

plain_text = f1.read()
print("Plaintext is: ", plain_text)

start_encrypt = time.time()*10e6
cipher_text = des1.encrypt(plain_text.encode("latin-1"))
end_encrypt = time.time()*10e6

print("Ciphertext is: ", cipher_text.decode("latin-1"))
print("Time taken to encrypt: ", end_encrypt - start_encrypt, 'μs');
encrypt_cost = end_encrypt - start_encrypt
f2.write(cipher_text.decode("latin-1"))
f1.close()
f2.close()

start_decrypt = time.time()*10e6
msg = des2.decrypt(cipher_text)
end_decrypt = time.time()*10e6

print("Original Message", msg.decode("latin-1"))
print("Time taken to decrypt: ", end_decrypt - start_decrypt, 'μs')
decrypt_cost = end_decrypt - start_decrypt
print('=' * 100)
