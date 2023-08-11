#!/usr/bin/env python
with open('03.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#101 301 501
#102 302 502
#103 303 503
#201 401 601
#202 402 602
#203 403 603
#'''
#lines=data.strip().split('\n')

triples=[]
triple=[]
column=0

import re
done=False
while not done:
    for line in lines:
        line=re.sub(' +',' ',line.strip())
        s=[int(v) for v in line.split(' ')]
        if column>len(s)-1:
            done=True
            break
        triple.append(s[column])
        if len(triple)==3:
            triples.append(triple)
            triple=[]
    column+=1

n=0
for s in triples:
    if s[0]+s[1]<=s[2] or s[1]+s[2]<=s[0] or s[0]+s[2]<=s[1]:
        continue
    n+=1

print(n)

