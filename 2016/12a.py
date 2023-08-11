#!/usr/bin/env python
with open('12.txt','r') as f:
    lines=f.read().strip().split('\n')

#data='''
#cpy 41 a
#inc a
#inc a
#dec a
#jnz a 2
#dec a
#'''
#lines=data.strip().split('\n')

regs={}
ip=-1

import re
while True:
    ip+=1
    if ip<0 or ip>len(lines)-1:
        print('halt')
        print(regs)
        exit()
    line=lines[ip]
    #print(ip,regs,line)
    #input()
    m=re.match(r'cpy (\d+) (\w)',line)
    if m:
        regs[m.group(2)]=int(m.group(1))
        continue
    m=re.match(r'cpy (\w) (\w)',line)
    if m:
        regs[m.group(2)]=regs.get(m.group(1),0)
        continue
    m=re.match(r'inc (\w)',line)
    if m:
        regs[m.group(1)]=regs.get(m.group(1),0)+1
        continue
    m=re.match(r'dec (\w)',line)
    if m:
        regs[m.group(1)]=regs.get(m.group(1),0)-1
        continue
    m=re.match(r'jnz (\d) (-?\d+)',line)
    if m:
        if int(m.group(1))!=0:
            ip+=int(m.group(2))-1
        continue
    m=re.match(r'jnz (\w) (-?\d+)',line)
    if m:
        if regs.get(m.group(1),0)!=0:
            ip+=int(m.group(2))-1
        continue

