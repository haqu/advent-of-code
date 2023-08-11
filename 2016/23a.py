#!/usr/bin/env python3
with open('23.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#cpy 2 a
#tgl a
#tgl a
#tgl a
#cpy 1 a
#dec a
#dec a
#'''
#lines=test.strip().split('\n')

regs={'a':7}
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
        if op1.isdigit() or op1[0]=='-':
            regs[op2]=int(op1)
        else:
            regs[op2]=regs.get(op1,0)
        continue
    elif line.startswith('jnz'):
        _,op1,op2,*_=line.split(' ')
        if op1.isdigit() or op1[0]=='-':
            op1=int(op1)
        else:
            op1=regs.get(op1,0)
        if op2.isdigit() or op2[0]=='-':
            op2=int(op2)
        else:
            op2=regs.get(op2,0)
        if op1!=0:
            ip+=op2-1
        continue
    elif line.startswith('tgl'):
        _,op,*_=line.split(' ')
        if op.isdigit() or op[0]=='-':
            ip2=ip+int(op)
        else:
            ip2=ip+regs.get(op,0)
        if ip2<0 or ip2>len(lines)-1:
            continue
        line2=lines[ip2]
        arr=line2.split(' ')
        if arr[0]=='inc':
            arr[0]='dec'
        elif arr[0]=='dec' or arr[0]=='tgl':
            arr[0]='inc'
        elif arr[0]=='cpy':
            arr[0]='jnz'
        elif arr[0]=='jnz':
            arr[0]='cpy'
        lines[ip2]=' '.join(arr)
        continue

