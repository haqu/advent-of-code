#!/usr/bin/env python
with open('23.txt','r') as f:
    lines=f.read().strip().split('\n')

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
    elif line.startswith('sub'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['sub',parse_op(op1),parse_op(op2)])
    elif line.startswith('mul'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['mul',parse_op(op1),parse_op(op2)])
    elif line.startswith('jnz'):
        _,op1,op2,*_=line.split(' ')
        instructions.append(['jnz',parse_op(op1),parse_op(op2)])

n_instructions=len(instructions)

regs={}
ip=-1
mul_counter=0

while True:
    ip+=1
    if ip<0 or ip>=n_instructions:
        print(mul_counter)
        exit()
    ins=instructions[ip]
    if ins[0]=='set':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op2[1],0)
            else:
                regs[op1[1]]=op2[1]
    elif ins[0]=='sub':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op1[1],0)-regs.get(op2[1],0)
            else:
                regs[op1[1]]=regs.get(op1[1],0)-op2[1]
    elif ins[0]=='mul':
        op1,op2=ins[1],ins[2]
        if op1[0]=='reg':
            if op2[0]=='reg':
                regs[op1[1]]=regs.get(op1[1],0)*regs.get(op2[1],0)
            else:
                regs[op1[1]]=regs.get(op1[1],0)*op2[1]
        mul_counter+=1
    elif ins[0]=='jnz':
        op1,op2=ins[1],ins[2]
        test_passed=False
        if op1[0]=='reg':
            if regs.get(op1[1],0)!=0:
                test_passed=True
        else:
            if op1[1]>0:
                test_passed=True
        if test_passed:
            if op2[0]=='reg':
                ip+=regs.get(op2[1],0)-1
            else:
                ip+=op2[1]-1

