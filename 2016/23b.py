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

# manual reverse engineering
# 6 - 8455             6!+7735
# 7 - 12775  (+4320)   7!+7735
# 8 - 48055  (+35280)  8!+7735
# 9 - 370615 (+322560) 9!+7735
# 12                   12!+7735 - 479009335
regs={'a':12}
ip=-1

code=[]
# 0 - inc
# 1 - dec
# 2 - tgl
# 3 - cpy
# 4 - jnz
for line in lines:
    if line.startswith('inc'):
        op=line.split(' ')[1]
        code.append([0,op])
        continue
    if line.startswith('dec'):
        op=line.split(' ')[1]
        code.append([1,op])
        continue
    if line.startswith('tgl'):
        op=line.split(' ')[1]
        inst=[2]
        if op.isdigit() or op[0]=='-':
            inst.append(int(op))
        else:
            inst.append(op)
        code.append(inst)
        continue
    if line.startswith('cpy'):
        _,op1,op2,*_=line.split(' ')
        inst=[3]
        if op1.isdigit() or op1[0]=='-':
            inst.append(int(op1))
        else:
            inst.append(op1)
        if op2.isdigit() or op2[0]=='-':
            inst.append(int(op2))
        else:
            inst.append(op2)
        code.append(inst)
        continue
    elif line.startswith('jnz'):
        _,op1,op2,*_=line.split(' ')
        inst=[4]
        if op1.isdigit() or op1[0]=='-':
            inst.append(int(op1))
        else:
            inst.append(op1)
        if op2.isdigit() or op2[0]=='-':
            inst.append(int(op2))
        else:
            inst.append(op2)
        code.append(inst)
        continue

while True:
    ip+=1
    if ip<0 or ip>len(code)-1:
        print('halt')
        print(regs)
        exit()
    inst=code[ip]
    #print(ip,regs,inst)
    #input()
    if inst[0]==0: # inc
        op=inst[1]
        regs[op]=regs.get(op,0)+1
    elif inst[0]==1: # dec
        op=inst[1]
        regs[op]=regs.get(op,0)-1
    elif inst[0]==2: # tgl
        op=inst[1]
        if isinstance(op,int):
            ip2=ip+op
        else:
            ip2=ip+regs.get(op,0)
        if ip2<0 or ip2>len(code)-1:
            continue
        inst2=code[ip2]
        if inst2[0]==0: # inc
            inst2[0]=1 # dec
        elif inst2[0]<=2: # dec, tgl
            inst2[0]=0 # inc
        elif inst2[0]==3: # cpy
            inst2[0]=4
        elif inst2[0]==4: # jnz
            inst2[0]=3
    elif inst[0]==3: # cpy
        op1=inst[1]
        op2=inst[2]
        if not isinstance(op2,int): # op2 is reg
            if isinstance(op1,int):
                regs[op2]=op1
            else:
                regs[op2]=regs.get(op1,0)
    elif inst[0]==4: # jnz
        op1=inst[1]
        op2=inst[2]
        not_zero=False
        if not isinstance(op1,int):
            op1=regs.get(op1,0)
        if not isinstance(op2,int):
            op2=regs.get(op2,0)
        if op1!=0:
            ip+=op2-1

