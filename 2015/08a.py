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

import codecs
decoder=codecs.getdecoder('unicode_escape')

n=0
for line in lines:
    l1=len(line)
    #print(l1)
    l2=len(decoder(line)[0])-2
    #print(l2)
    n+=l1-l2

print(n)
