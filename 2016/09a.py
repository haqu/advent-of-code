#!/usr/bin/env python
with open('09.txt','r') as f:
    data=f.read().strip()

# test
#data='''
#X(8x2)(3x3)ABCY
#'''.strip()

import re
decompressed=''
i=0
inside_marker=False
while i<len(data):
    if not inside_marker:
        if data[i]=='(':
            m=re.match(r'\((\d+)x(\d+)\)',data[i:]).groups()
            l=int(m[0])
            r=int(m[1])
            inside_marker=True
        else:
            decompressed+=data[i]
    else:
        if data[i]==')':
            inside_marker=False
            part=data[i+1:i+1+l]
            decompressed+=part*r
            i+=l
    i+=1

#print(decompressed)
print(len(decompressed))

