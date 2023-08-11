#!/usr/bin/env python
with open('02.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#ULL
#RRDDD
#LURDL
#UUUUD
#'''
#lines=data.strip().split('\n')

# 1 2 3
# 4 5 6
# 7 8 9

dirs=['U','D','L','R']
coord=[1,1]
digits=''

for line in lines:
    commands=list(line)
    for c in commands:
        if c=='U' and coord[1]>0:
            coord[1]-=1
        elif c=='D' and coord[1]<2:
            coord[1]+=1
        elif c=='L' and coord[0]>0:
            coord[0]-=1
        elif c=='R' and coord[0]<2:
            coord[0]+=1
    digit=coord[0]+1+coord[1]*3
    digits+=str(digit)

print(digits)

