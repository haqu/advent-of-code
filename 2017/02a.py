#!/usr/bin/env python3
with open('02.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#5 1 9 5
#7 5 3
#2 4 6 8
#'''
#lines=test.strip().split('\n')

csum=0
for line in lines:
    values=[int(v) for v in line.split()]
    diff=max(values)-min(values)
    csum+=diff
print(csum)

