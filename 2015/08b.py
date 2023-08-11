#!/usr/bin/env python
with open('08.txt','r') as f:
    lines=f.read().strip().split('\n')

#data='''
#""
#"abc"
#"aaa\\"aaa"
#"\\x27"
#'''
#lines=data.strip().split('\n')

import re

n=0
for line in lines:
    delta=len(re.findall(r'["\\]',line))+2
    n+=delta

print(n)

