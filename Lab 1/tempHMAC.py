# #Following code reads its source file and computes an HMAC signature for it:
# import hmac
# secret_key = 'secret-shared-key-goes-here'
# digest_maker = hmac.new(secret_key)#in your code replace key
# f = open('lorem.txt', 'rb')
# try:
#     while True:
#         block = f.read(1024)
#         if not block:
#             break
#         digest_maker.update(block)
# finally:
#     f.close()

# digest = digest_maker.hexdigest()
# print('='*100)
# print("HMAC digest generated for \"lorem.txt\" file is:", digest)
# print('='*100)
import hmac
import sys
import time
import os
def main(inputfile):
    time_start = time.time()
    secret_key = 'secret-shared-key-goes-here'
    digest_maker = hmac.new(secret_key.encode("latin-1"), digestmod='MD5')#in your code replace key
    f = open(inputfile, 'rb')
    try:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()
    
    digest = digest_maker.hexdigest()
    time_end = time.time()
    print('='*100)
    print("HMAC digest generated for " + inputfile + " file is:", digest)
    print('='*100)
    time_cost = time_end - time_start
    folder = os.getcwd() + "\\test_result\\"
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open("test_result\\HMAC_" + inputfile, 'w', encoding='utf-8') as file_object:
        file_object.write("time cost: " + str(time_cost) + 's')

if __name__ == "__main__":
    try:
        inputfile= sys.argv[1]
        main(inputfile)
    except Exception as e:
        print(e)
