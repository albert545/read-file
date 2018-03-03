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

#篩選清單
#留言長度小於100

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('共有',len(new),'筆留言小於100的長度')
print(new[0])

#留言包含"good"的留言、筆數
good =[]
for d in data:
    if 'good' in d:
        good.append(d)
print('共有',len(good),'筆留言中包含''good''')
print(good[0])

#list 清單快寫法
good=[d for d in data if 'good' in d]
print(len(good))

#print(data[0])
#print('---------------------------------')
#print(data[2])
#print('---------------------------------')