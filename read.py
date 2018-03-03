# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:11:36 2018

@author: albert-w10
"""

data = []
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
print(len(data))

print(data[0])
print('---------------------------------')
print(data[2])
print('---------------------------------')