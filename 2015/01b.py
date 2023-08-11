#!/usr/bin/env python
with open('01.txt','r') as f:
    data=f.read()
#data='(())'
#data='))((((('
#data='))('
c=0
i=0
for ch in data:
    i+=1
    if ch=='(':
        c+=1
    elif ch==')':
        c-=1
    if c<0:
        print(i)
        exit()

