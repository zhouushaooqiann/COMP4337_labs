# import hashlib

# #initializing string
# print('='*100)
# str = "SHA1 Clear text"
  
# result = hashlib.sha1(str.encode()) 
  
# # printing the equivalent hexadecimal value. 
# print("The hexadecimal equivalent of SHA1 digest is : ") 
# print(result.hexdigest())
# print('='*100)
import hashlib
import time
import sys
import os
def main(inputfile):
    time_start = time.time()
    #initializing string
    print('='*100)
    with open(inputfile, 'r') as f:
        st = f.read()
      
    result = hashlib.sha1(st.encode()) 
    time_end = time.time()
    # printing the equivalent hexadecimal value. 
    print("The hexadecimal equivalent of SHA1 digest is : ") 
    print(result.hexdigest())
    print('='*100)
    time_cost = time_end - time_start
    folder = os.getcwd() + "\\test_result\\"
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open("test_result\\sha1_" + inputfile, 'w', encoding='utf-8') as file_object:
        file_object.write("time cost: " + str(time_cost) + 's')

if __name__ == "__main__":
    try:
        inputfile= sys.argv[1]
        main(inputfile)
    except Exception as e:
        print(e)
