#!/usr/bin/env python

data='cqjxjnds'

def increment(s):
    s2=s[:-1]
    if s[-1:]=='z':
        s2=increment(s2)
        c2='a'
    else:
        c2=chr(ord(s[-1:])+1)
    return s2+c2

while True:
    data=increment(data)
    if 'i' in data or 'o' in data or 'l' in data:
        continue
    found=False
    for i in range(len(data)-2):
        if ord(data[i])==ord(data[i+1])-1 and ord(data[i+1])==ord(data[i+2])-1:
               found=True
               break
    if not found:
        continue
    n_pairs=0
    i=0
    while i<len(data)-1:
        if data[i]==data[i+1]:
            n_pairs+=1
            if n_pairs==2:
                break
            i+=1
        i+=1
    if n_pairs!=2:
        continue
    print(data)
    break

