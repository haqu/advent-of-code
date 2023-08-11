#!/usr/bin/env python
with open('03.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#5 10 25
#'''
#lines=data.strip().split('\n')

import re
n=0
for line in lines:
    line=re.sub(' +',' ',line.strip())
    s=[int(v) for v in line.split(' ')]
    if s[0]+s[1]<=s[2] or s[1]+s[2]<=s[0] or s[0]+s[2]<=s[1]:
        continue
    n+=1
print(n)

