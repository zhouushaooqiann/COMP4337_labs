# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:34:22 2022

@author: sola
"""
import sys
size = [16, 64, 512, 4096, 32768, 262144, 2047152]
for i in range(len(size)):
    with open("b_test_" + str(size[i]) + ".txt", 'w', encoding='utf-8') as file_object:
        file_object.write('A'*size[i])
size_rsa = [2, 4, 8, 16, 32, 64]
for i in range(len(size_rsa)):
    with open("b_RSA_test_" + str(size_rsa[i]) + ".txt", 'w', encoding='utf-8') as file_object:
        file_object.write('A'*size_rsa[i])
