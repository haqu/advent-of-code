#!/usr/bin/env python
with open('18.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#snd 1
#snd 2
#snd p
#rcv a
#rcv b
#rcv c
#rcv d
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

p0_regs={'p':0}
p1_regs={'p':1}
p0_ip=-1
p1_ip=-1
p0_snd=[]
p1_snd=[]
p0_waiting=False
p1_waiting=False
p0_terminated=False
p1_terminated=False
p1_snd_counter=0

while True:
    if not p0_terminated and not p0_waiting:
        p0_ip+=1
        if p0_ip<0 or p0_ip>=n_instructions:
            p0_terminated=True
        else:
            ins=instructions[p0_ip]
            if ins[0]=='set':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p0_regs[op1[1]]=p0_regs.get(op2[1],0)
                    else:
                        p0_regs[op1[1]]=op2[1]
            elif ins[0]=='add':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)+p0_regs.get(op2[1],0)
                    else:
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)+op2[1]
            elif ins[0]=='mul':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)*p0_regs.get(op2[1],0)
                    else:
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)*op2[1]
            elif ins[0]=='mod':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)%p0_regs.get(op2[1],0)
                    else:
                        p0_regs[op1[1]]=p0_regs.get(op1[1],0)%op2[1]
            elif ins[0]=='jgz':
                op1,op2=ins[1],ins[2]
                test_passed=False
                if op1[0]=='reg':
                    if p0_regs.get(op1[1],0)>0:
                        test_passed=True
                else:
                    if op1[1]>0:
                        test_passed=True
                if test_passed:
                    if op2[0]=='reg':
                        p0_ip+=p0_regs.get(op2[1],0)-1
                    else:
                        p0_ip+=op2[1]-1
            elif ins[0]=='snd':
                op1=ins[1]
                if op1[0]=='reg':
                    p0_snd.append(p0_regs.get(op1[1],0))
                else:
                    p0_snd.append(op1[1])
                if p1_waiting:
                    p1_waiting=False
            elif ins[0]=='rcv':
                op1=ins[1]
                if op1[0]=='reg':
                    if len(p1_snd)==0:
                        p0_waiting=True
                        p0_ip-=1
                    else:
                        p0_regs[op1[1]]=p1_snd.pop(0)
    if not p1_terminated and not p1_waiting:
        p1_ip+=1
        if p1_ip<0 or p1_ip>=n_instructions:
            p1_terminated=True
        else:
            ins=instructions[p1_ip]
            if ins[0]=='set':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p1_regs[op1[1]]=p1_regs.get(op2[1],0)
                    else:
                        p1_regs[op1[1]]=op2[1]
            elif ins[0]=='add':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)+p1_regs.get(op2[1],0)
                    else:
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)+op2[1]
            elif ins[0]=='mul':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)*p1_regs.get(op2[1],0)
                    else:
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)*op2[1]
            elif ins[0]=='mod':
                op1,op2=ins[1],ins[2]
                if op1[0]=='reg':
                    if op2[0]=='reg':
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)%p1_regs.get(op2[1],0)
                    else:
                        p1_regs[op1[1]]=p1_regs.get(op1[1],0)%op2[1]
            elif ins[0]=='jgz':
                op1,op2=ins[1],ins[2]
                test_passed=False
                if op1[0]=='reg':
                    if p1_regs.get(op1[1],0)>0:
                        test_passed=True
                else:
                    if op1[1]>0:
                        test_passed=True
                if test_passed:
                    if op2[0]=='reg':
                        p1_ip+=p1_regs.get(op2[1],0)-1
                    else:
                        p1_ip+=op2[1]-1
            elif ins[0]=='snd':
                op1=ins[1]
                if op1[0]=='reg':
                    p1_snd.append(p1_regs.get(op1[1],0))
                else:
                    p1_snd.append(op1[1])
                if p0_waiting:
                    p0_waiting=False
                p1_snd_counter+=1
            elif ins[0]=='rcv':
                op1=ins[1]
                if op1[0]=='reg':
                    if len(p0_snd)==0:
                        p1_waiting=True
                        p1_ip-=1
                    else:
                        p1_regs[op1[1]]=p0_snd.pop(0)
    if p0_waiting and p1_waiting:
        p0_terminated=True
        p1_terminated=True
    if p0_terminated and p1_terminated:
        print(p1_snd_counter)
        exit()

