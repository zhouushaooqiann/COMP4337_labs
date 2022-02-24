import sys
from Crypto.Cipher import DES
from Crypto import Random

# acquire parameters
iv = sys.argv[1]
key = sys.argv[2]
inputfile = sys.argv[3]
f1 = open(inputfile, 'r')
outputfile = sys.argv[4]
f2 = open(outputfile, 'w',encoding = "latin-1")

#cbc_key = Random.get_random_bytes(8)

print('=' * 100)
print('Key used: ', [x for x in key])


#iv = Random.get_random_bytes(8)

print("IV used: ", [x for x in iv])
print('=' * 100)

des1 = DES.new(bytearray.fromhex(key), DES.MODE_CBC, bytearray.fromhex(iv))
des2 = DES.new(bytearray.fromhex(key), DES.MODE_CBC, bytearray.fromhex(iv))

plain_text = f1.read()
print("Plaintext is: ", plain_text)


cipher_text = des1.encrypt(plain_text.encode("latin-1"))


print("Ciphertext is: ", cipher_text.decode("latin-1"))

f2.write(cipher_text.decode("latin-1"))
f1.close()
f2.close()

msg = des2.decrypt(cipher_text)
print("Original Message", msg.decode("latin-1"))

print('=' * 100)