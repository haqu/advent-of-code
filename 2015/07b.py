#!/usr/bin/env python
with open('07.txt','r') as f:
    lines=f.read().strip().split('\n')

#test
#data='''
#123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i
#'''
#lines=data.strip().split('\n')

import re
wire_re=re.compile(r'[a-z]+')

wires={}

def check_v(op):
    if wire_re.match(op):
        return (wires.get(op)!=None)
    return True

def get_v(op):
    if wire_re.match(op):
        return wires.get(op,0)
    return int(op)

completed_lines=0
total_lines=len(lines)
current_line=-1
while completed_lines<total_lines:
    current_line+=1
    line=lines[current_line]
    lpart,rpart,*_=line.split(' -> ')
    if 'AND' in lpart:
        op1,op2,*_=lpart.split(' AND ')
        if not check_v(op1) or not check_v(op2):
            lines.append(line)
            continue
        wires[rpart]=get_v(op1)&get_v(op2)
    elif 'OR' in lpart:
        op1,op2,*_=lpart.split(' OR ')
        if not check_v(op1) or not check_v(op2):
            lines.append(line)
            continue
        wires[rpart]=get_v(op1)|get_v(op2)
    elif 'NOT' in lpart:
        _,op,*_=lpart.split('NOT ')
        if not check_v(op):
            lines.append(line)
            continue
        wires[rpart]=~get_v(op)&65535
    elif 'LSHIFT' in lpart:
        op1,op2,*_=lpart.split(' LSHIFT ')
        if not check_v(op1) or not check_v(op2):
            lines.append(line)
            continue
        wires[rpart]=get_v(op1)<<get_v(op2)
    elif 'RSHIFT' in lpart:
        op1,op2,*_=lpart.split(' RSHIFT ')
        if not check_v(op1) or not check_v(op2):
            lines.append(line)
            continue
        wires[rpart]=get_v(op1)>>get_v(op2)
    else:
        if not check_v(lpart):
            lines.append(line)
            continue
        wires[rpart]=get_v(lpart)
        if rpart=='b':
            wires[rpart]=3176
    #print('line:',line)
    completed_lines+=1

#for w in wires:
#    print(f'{w}: {wires[w]}')

print('a:',wires['a']);
print('b:',wires['b']);

