#!/usr/bin/env python

data='1321131112'

for _ in range(40):
    data1=''
    for i in range(len(data)):
        c=data[i]
        if i==0:
            pc=c
            n=1
        elif c!=pc:
            data1+=str(n)
            data1+=pc
            pc=c
            n=1
        else:
            n+=1
    data1+=str(n)
    data1+=pc
    data=data1

print(len(data1))

