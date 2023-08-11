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

regs={'c':1}
ip=-1

while True:
    ip+=1
    if ip<0 or ip>len(lines)-1:
        print('halt')
        print(regs)
        exit()
    line=lines[ip]
    #print(ip,regs,line)
    #input()
    if line.startswith('inc'):
        op=line.split(' ')[1]
        regs[op]=regs.get(op,0)+1
        continue
    if line.startswith('dec'):
        op=line.split(' ')[1]
        regs[op]=regs.get(op,0)-1
        continue
    if line.startswith('cpy'):
        _,op1,op2,*_=line.split(' ')
        if op1.isdigit():
            regs[op2]=int(op1)
        else:
            regs[op2]=regs.get(op1,0)
        continue
    elif line.startswith('jnz'):
        _,op1,op2,*_=line.split(' ')
        if op1.isdigit():
            if int(op1)!=0:
                ip+=int(op2)-1
        else:
            if regs.get(op1,0)!=0:
                ip+=int(op2)-1
        continue

