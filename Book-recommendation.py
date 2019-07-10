#!/usr/bin/env python
 # -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import datetime
from sklearn import preprocessing
starttime = datetime.datetime.now()

# 读取借阅记录:编号,证件号,单位,借书日期,（应）还书日期,书刊条码号,题名,索书号,馆藏地.
dt=pd.read_table('C:\\Users\\wjp\\Desktop\\2014A.txt',sep=',',header=0,encoding='gbk')
dt = dt.iloc[0:20000,:]
dt.dropna(inplace=True)
dt.columns = ['A','B','C','D','E','F','G','H','I']
dt.drop(['A'],axis=1,inplace=True)
dt.drop_duplicates(inplace=True)
# for i in ['B','C','F','G','H','I']:
label = preprocessing.LabelEncoder()
label.fit(dt['B'])
dt['B'] = label.transform(dt['B'])
# dt.D = pd.to_datetime(dt['D'])
# data_new1 = pd.to_datetime('2014-01-01')
# dt.D = dt.D - data_new1
#
# dt.E = pd.to_datetime(dt['E'])
# data_new2 = pd.to_datetime('2014-01-01')
# dt.E = dt.E - data_new2

def UserS(train,u):
    w = dict()
    # for u in train.keys():
    w[u] = dict()
    for v in train.keys():
        if u == v:
            w[u][v] = 0
        w[u][v] = len(list(set(train[u]).intersection(set(train[v]))))*1.0
        w[u][v] /= len(list(set(train[u]).union(set(train[v]))))*1.0
    return w
def getRank(w,b,dic,u):
    rank = [0] * len(b)
    for i,j in enumerate(b):
        for k,l in dic.items():
            if l == u:
                rank[i] = -10000
            elif j in l:
                rank[i] += w[u][k]
    return rank
dic = {}
for i in range(len(set(dt.B))):
    dic[i] = list(dt[dt.B==i]['G'])
b = list(set(dt.G))
a = int(input('请输入学生证件号：'))
w = UserS(dic,a)
rank = getRank(w,b,dic,a)

def get_index(nums,k):
    temp=[]
    Inf = 0
    for i in range(k):
        temp.append(nums.index(max(nums)))
        nums[nums.index(max(nums))]=Inf
    temp.sort()
    return temp
get_book = []
for i in get_index(rank,8):
    get_book.append(b[i])
# data['time_d'].head()
# dt.索书号 = preprocessing.LabelEncoder().fit_transform(dt.索书号)
# # zheng=dt.iloc[:,[1]]
# # suo = dt.iloc[:,[7]]
# # d1 = preprocessing.LabelEncoder().fit_transform(zheng)
# # d2 = preprocessing.LabelEncoder().fit_transform(suo)
# #
# # dt.索书号 = d2.inverse_transform(dt.索书号)
# print(dt)
# for i in get_book:
#     if i not in dic[a]:
#         print('为该生推荐书目：',i)
endtime = datetime.datetime.now()
print '运行时间：'+str((endtime - starttime).seconds)

# # print rank
# for i in get_book:
#     if i not in dic[a]:
#         print('为该生推荐书目：',i)
# print i
# dic[a]
print '借过的书：'
for i in dic[a]:
    print i

print('-----')
print ('推荐书目：')
for i in get_book:
    print i

