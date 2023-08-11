#!/usr/bin/env python
with open('18.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#set a 1
#add a 2
#mul a a
#mod a 5
#snd a
#set a 0
#rcv a
#jgz a -1
#set a 1
#jgz a -2
#'''.strip().split('\n')

instructions=[]

def parse_op(op):
    if op.isdigit():
        return ('num',int(op))
    if op[0]=='-' and op[1:].isdigit():
        return ('num',-int(op[1:]))
    return ('reg',op)

for line in lines:
    if line.startswith('set'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['set',parse_op(op1),parse_op(op2)])
    elif line.startswith('add'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['add',parse_op(op1),parse_op(op2)])
    elif line.startswith('mul'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['mul',parse_op(op1),parse_op(op2)])
    elif line.startswith('mod'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['mod',parse_op(op1),parse_op(op2)])
    elif line.startswith('jgz'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['jgz',parse_op(op1),parse_op(op2)])
    elif line.startswith('snd'):
        _,op1,*_=line.split(' ')
        instructions.append(['snd',parse_op(op1)])
    elif line.startswith('rcv'):
        _,op1,*_=line.split(' ')
        instructions.append(['rcv',parse_op(op1)])

n_instructions=len(instructions)

regs={}
ip=-1
while True:
    ip+=1
    if ip<0 or ip>=n_instructions:
        print('terminated')
        exit()
    ins=instructions[ip]
    if ins[0]=='set':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op2[1],0)
            else:
                regs[op1[1]]=op2[1]
    elif ins[0]=='add':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op1[1],0)+regs.get(op2[1],0)
            else:
                regs[op1[1]]=regs.get(op1[1],0)+op2[1]
    elif ins[0]=='mul':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op1[1],0)*regs.get(op2[1],0)
            else:
                regs[op1[1]]=regs.get(op1[1],0)*op2[1]
    elif ins[0]=='mod':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op1[1],0)%regs.get(op2[1],0)
            else:
                regs[op1[1]]=regs.get(op1[1],0)%op2[1]
    elif ins[0]=='jgz':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if regs.get(op1[1],0)==0:
                continue
        else:
            if op1[1]==0:
                continue
        if op2[0]=='reg':
            ip+=regs.get(op2[1],0)-1
        else:
            ip+=op2[1]-1
    elif ins[0]=='snd':
        op1=ins[1]
        if op1[0]=='reg':
            regs['snd']=regs.get(op1[1],0)
        else:
            regs['snd']=op1[1]
    elif ins[0]=='rcv':
        print(regs.get('snd',0))
        exit()

