#!/usr/bin/env python3
with open('25.txt','r') as f:
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

initial_a=0
while True:
    initial_a+=1
    regs={'a':initial_a}
    ip=-1
    valid_outputs=0
    prev_v=1
    while True:
        ip+=1
        if ip<0 or ip>len(lines)-1:
            break
        line=lines[ip]
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
        elif line.startswith('out'):
            _,op,*_=line.split(' ')
            v=regs[op]
            if prev_v==0 and v==1:
                valid_outputs+=1
            elif prev_v==1 and v==0:
                valid_outputs+=1
            else:
                break
            prev_v=v
            if valid_outputs==10:
                print('10 valid outputs in a row')
                print(f'initial a: {initial_a}')
                exit()

