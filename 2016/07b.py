#!/usr/bin/env python
with open('07.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#aba[bab]xyz
#xyx[xyx]xyx
#aaa[kek]eke
#zazbz[bzb]cdb
#'''
#lines=data.strip().split('\n')

def find_aba(s):
    arr=[]
    ls=len(s)
    if ls<3:
        return False
    for i in range(ls-2):
        if s[i]!=s[i+1] and s[i]==s[i+2]:
            arr.append(s[i:i+3])
    return arr

import re
n=0
for line in lines:
    groups=re.findall(r'\w+',line)
    abas=[]
    babs=[]
    for i in range(0,len(groups),2):
        abas+=find_aba(groups[i])
    for i in range(1,len(groups),2):
        babs+=find_aba(groups[i])
    for aba in abas:
        bab=aba[1]+aba[0]+aba[1]
        if bab in babs:
            n+=1
            break
print(n)

