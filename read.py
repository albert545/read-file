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
        if count % 100000 == 0:
            print(len(data))
print('檔案讀取完了共有',len(data),'筆資料')

#留言平均長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言平均長度是:',sum_len / len(data))

#print(data[0])
#print('---------------------------------')
#print(data[2])
#print('---------------------------------')