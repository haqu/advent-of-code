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

keypad_str='''
. . 1 . .
. 2 3 4 .
5 6 7 8 9
. A B C .
. . D . .
'''
keypad=keypad_str.strip().replace('\n',' ').split(' ')

dirs=['U','D','L','R']
coord=[0,2]
digits=''

for line in lines:
    commands=list(line)
    for c in commands:
        coord2=coord.copy()
        if c=='U' and coord[1]>0:
            coord2[1]-=1
        elif c=='D' and coord[1]<4:
            coord2[1]+=1
        elif c=='L' and coord[0]>0:
            coord2[0]-=1
        elif c=='R' and coord[0]<4:
            coord2[0]+=1
        if keypad[coord2[0]+coord2[1]*5]!='.':
            coord=coord2
    digit=keypad[coord[0]+coord[1]*5]
    digits+=str(digit)

print(digits)

