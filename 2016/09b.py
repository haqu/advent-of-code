#!/usr/bin/env python
with open('09.txt','r') as f:
    data=f.read().strip()

# test
#data='''
#(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN
#'''.strip()

import re
def decompress(s):
    n=0
    i=0
    inside_marker=False
    while i<len(s):
        if not inside_marker:
            if s[i]=='(':
                m=re.match(r'\((\d+)x(\d+)\)',s[i:]).groups()
                l=int(m[0])
                r=int(m[1])
                inside_marker=True
            else:
                n+=1
        else:
            if s[i]==')':
                inside_marker=False
                n+=r*decompress(s[i+1:i+1+l])
                i+=l
        i+=1
    return n

print(decompress(data))

