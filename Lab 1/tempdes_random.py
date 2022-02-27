import sys
import time
from Crypto.Cipher import DES
from Crypto import Random
import os
# acquire parameters
inputfile = sys.argv[1]

try:
    f1 = open(inputfile, 'r', encoding = "latin-1")
except Exception as e:
    print(e)


cbc_key = Random.get_random_bytes(8)

print('=' * 100)
print('Key used: ', [x for x in cbc_key])


iv = Random.get_random_bytes(8)

print("IV used: ", [x for x in iv])
print('=' * 100)

try:
    des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
    des2 = DES.new(cbc_key, DES.MODE_CBC, iv)
except Exception as e:
    print(e)

plain_text = f1.read()

start_encrypt = time.time()*10e6
cipher_text = des1.encrypt(plain_text.encode("latin-1"))
end_encrypt = time.time()*10e6

print("Time taken to encrypt: ", end_encrypt - start_encrypt, 'μs');
encrypt_cost = end_encrypt - start_encrypt

f1.close()


start_decrypt = time.time()*10e6
msg = des2.decrypt(cipher_text)
end_decrypt = time.time()*10e6

print("Time taken to decrypt: ", end_decrypt - start_decrypt, 'μs')
decrypt_cost = end_decrypt - start_decrypt
print('=' * 100)
folder = os.getcwd() + "\\test_result\\"
if not os.path.exists(folder):
    os.makedirs(folder)
with open("test_result\\des_" + inputfile, 'w', encoding='utf-8') as file_object:
    file_object.write("encrypt time cost: " + str(encrypt_cost) + 'μs' + 
                      "\ndecrypt time cost: " + str(decrypt_cost) + 'μs')
