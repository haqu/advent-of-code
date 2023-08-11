#!/usr/bin/env python3
with open('02.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#5 9 2 8
#9 4 7 3
#3 8 6 5
#'''
#lines=test.strip().split('\n')

res=0
for line in lines:
    values=[int(v) for v in line.split()]
    values.sort(reverse=True)
    found=False
    for i in range(len(values)-1):
        v1=values[i]
        for i2 in range(i+1,len(values)):
            v2=values[i2]
            if v1%v2==0:
                res+=int(v1/v2)
                found=True
                break
        if found:
            break

print(res)

