#!/usr/bin/env python
with open('07.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#abba[mnop]qrst
#abcd[bddb]xyyx
#aaaa[qwer]tyui
#ioxxoj[asdfgh]zxcvbn
#'''
#lines=data.strip().split('\n')

def check_abba(s):
    ls=len(s)
    if ls<4:
        return False
    for i in range(ls-3):
        if s[i]!=s[i+1] and s[i]==s[i+3] and s[i+1]==s[i+2]:
            return True
    return False

import re
n=0
for line in lines:
    valid1=False
    valid2=True
    for i,m in enumerate(re.findall(r'\w+',line)):
        if i%2==0:
            if check_abba(m):
                valid1=True
        else:
            if check_abba(m):
                valid2=False
                break
    if valid1 and valid2:
        n+=1
print(n)

