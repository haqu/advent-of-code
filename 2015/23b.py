#!/usr/bin/env python

with open('23.txt','r') as f:
    lines=f.read().strip().split('\n')

n_lines=len(lines)
r={'a':1,'b':0}

ip=0
while True:
    if ip<0 or ip>n_lines-1:
        print('error')
        exit()
    line=lines[ip].replace(',','')
    ins,*ops=line.split(' ')
    if ins=='inc':
        r[ops[0]]+=1
    elif ins=='tpl':
        r[ops[0]]*=3
    elif ins=='hlf':
        r[ops[0]]/=2
    elif ins=='jmp':
        ip+=int(ops[0])-1
    elif ins=='jie':
        if r[ops[0]]%2==0:
            ip+=int(ops[1])-1
    elif ins=='jio':
        if r[ops[0]]==1:
            ip+=int(ops[1])-1
    else:
        print('unknown instruction: ',ins)
        exit()
    a,b=r['a'],r['b']
    print(f'ip:{ip} ins:{ins} a:{a} b:{b}')
    ip+=1

