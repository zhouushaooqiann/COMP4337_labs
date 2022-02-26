# import Crypto
# from Crypto.PublicKey import RSA
# from Crypto import Random
# import ast

# random_generator = Random.new().read
# key = RSA.generate(1024, random_generator)  # generate pub and priv key

# publickey = key.publickey()  # pub key export for exchange

# print('=' * 100)
# plain_text = 'abcdefghijklmnopqrst'
# print("Plaintext is: ", plain_text)
# # print

# cipher_text = publickey.encrypt(plain_text, 32)  # message to encrypt is in the above line 'encrypt this message'
# print('Plaintext encrypted using Public Key is:', cipher_text)
# # print
# # decrypted code below
# decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
# print('Ciphertext decrypted with Private key is', decrypted)
# print('=' * 100)
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP
import sys
import time
import os
def main(inputfile):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)  # generate pub and priv key
    
    publickey = key.publickey()  # pub key export for exchange
    
    print('=' * 100)
    with open(inputfile, 'r') as f:
        plain_text = f.read()
    print("Plaintext is: ", plain_text)
    # print
    encryptor = PKCS1_OAEP.new(publickey)
    time_start = time.time()
    cipher_text = encryptor.encrypt(plain_text.encode("latin-1"))  # message to encrypt is in the above line 'encrypt this message'
    time_end = time.time()
    print('Plaintext encrypted using Public Key is:', cipher_text.decode("latin-1"))
    encrypt_cost = time_end - time_start

    # print
    # decrypted code below
    decryptor = PKCS1_OAEP.new(key)
    time_start = time.time()
    decrypted = decryptor.decrypt(ast.literal_eval(str(cipher_text)))
    time_end = time.time()
    print('Ciphertext decrypted with Private key is', decrypted.decode("latin-1"))
    decrypt_cost = time_end - time_start
    print('=' * 100)
    folder = os.getcwd() + "\\test_result\\"
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open("test_result\\rsa_" + inputfile, 'w', encoding='utf-8') as file_object:
        file_object.write("encrypt time cost: " + str(encrypt_cost) + 's' + "\ndecrypt time cost: " + str(decrypt_cost) + 's')

if __name__ == "__main__":
    try:
        inputfile= sys.argv[1]
        main(inputfile)
    except Exception as e:
        print(e)
