# from Crypto.Cipher import AES
# from Crypto import Random

# cbc_key = Random.get_random_bytes(16)
# print('=' * 100)
# print('Key used: ', [x for x in cbc_key])

# iv = Random.get_random_bytes(16)
# print("IV used: ", [x for x in iv])
# print('=' * 100)
# aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
# aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

# plain_text = 'hello world 1234'  # <- 16 bytes
# print("Plaintext is: ", plain_text)

# cipher_text = aes1.encrypt(plain_text)
# print("Ciphertext is: ", cipher_text)

# msg = aes2.decrypt(cipher_text)
# print("Decrypted message: ", msg)
# print('=' * 100)

from Crypto.Cipher import AES
from Crypto import Random
import time
import sys
import os
def main(inputfile):
    cbc_key = Random.get_random_bytes(16)
    print('=' * 100)
    print('Key used: ', [x for x in cbc_key])
    
    iv = Random.get_random_bytes(16)
    print("IV used: ", [x for x in iv])
    print('=' * 100)
    aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
    aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)
    
    with open(inputfile, 'r') as f:
        plain_text = f.read()
    print("Plaintext is: ", plain_text)
    
    time_start = time.time()
    cipher_text = aes1.encrypt(plain_text.encode("latin-1"))
    time_end = time.time()
    print("Ciphertext is: ", cipher_text.decode("latin-1"))
    encrypt_cost = time_end - time_start
    print("time cost: ", encrypt_cost, 's')
    
    time_start = time.time()
    msg = aes2.decrypt(cipher_text)
    time_end = time.time()
    print("Decrypted message: ", msg.decode("latin-1"))
    decrypt_cost = time_end - time_start
    print("time cost: ", decrypt_cost, 's')
    print('=' * 100)
    folder = os.getcwd() + "\\test_result\\"
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open("test_result\\aes_" + inputfile, 'w', encoding='utf-8') as file_object:
        file_object.write("encrypt time cost: " + str(encrypt_cost) + 's' + 
                          "\ndecrypt time cost: " + str(decrypt_cost) + 's')

if __name__ == "__main__":
    try:
        inputfile= sys.argv[1]
        main(inputfile)
    except Exception as e:
        print(e)
