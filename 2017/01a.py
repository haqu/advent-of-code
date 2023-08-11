#!/usr/bin/env python3
with open('01.txt','r') as f:
    data=f.read().strip()

#test
#data='1122'
#data='91212129'

res=0
datalen=len(data)
for i in range(datalen):
    i2=i+1
    if i2>datalen-1:
        i2=0
    v1=int(data[i])
    v2=int(data[i2])
    if v1==v2:
        res+=v1
print(res)

