#!/usr/bin/env python
with open('08.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10
#'''.strip().split('\n')

regs={}
max_value=0

for line in lines:
    r,cmd,v,_,r2,cmp,v2,*_=line.split(' ')
    if cmp=='>':
        if regs.get(r2,0)<=int(v2):
            continue
    elif cmp=='>=':
        if regs.get(r2,0)<int(v2):
            continue
    elif cmp=='<':
        if regs.get(r2,0)>=int(v2):
            continue
    elif cmp=='<=':
        if regs.get(r2,0)>int(v2):
            continue
    elif cmp=='==':
        if regs.get(r2,0)!=int(v2):
            continue
    elif cmp=='!=':
        if regs.get(r2,0)==int(v2):
            continue
    if cmd=='inc':
        regs[r]=regs.get(r,0)+int(v)
    elif cmd=='dec':
        regs[r]=regs.get(r,0)-int(v)
    for v in regs.values():
        if v>max_value:
            max_value=v

print(max_value)

