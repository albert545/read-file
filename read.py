# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:11:36 2018

@author: albert-w10
"""

data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 10000 == 0:
            print(len(data))
print(len(data))

print(data[0])
print('---------------------------------')
print(data[2])
print('---------------------------------')