#!/usr/bin/env python
a='10011111011011001'
ds=272

# test
#a='10000'
#ds=20

def invert(s):
    s2=''
    for c in reversed(s):
        if c=='0':
            s2+='1'
        else:
            s2+='0'
    return s2

dd=''
while True:
    a=a+'0'+invert(a)
    if len(a)>=ds:
        dd=a[:ds]
        break

def checksum(s):
    s2=''
    for i in range(0,len(s),2):
        if s[i]==s[i+1]:
            s2+='1'
        else:
            s2+='0'
    return s2

c=dd
while True:
    c=checksum(c)
    if len(c)%2==1:
        break

print(c)

