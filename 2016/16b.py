#!/usr/bin/env python
a='10011111011011001'
ds=35651584

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
print('generating data')
while True:
    a=a+'0'+invert(a)
    datalen=len(a)
    print(f'len: {datalen}')
    if datalen>=ds:
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
print('finding checksum')
while True:
    c=checksum(c)
    clen=len(c)
    print(f'len: {clen}')
    if clen%2==1:
        break

print(c)

