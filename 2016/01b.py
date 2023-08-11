#!/usr/bin/env python
with open('01.txt','r') as f:
    data=f.read()

# test
#data='R8, R4, R4, R8'

commands=[]
for part in data.split(', '):
    commands.append([part[0],int(part[1:])])
#print(commands)

dirs=['N','E','S','W']
ndirs=len(dirs)
dir_index=0
cx,cy,cx1,cy1=0,0,0,0
mem=[[cx,cy]]
for cmd in commands:
    if cmd[0]=='R':
        i=dir_index+1
        if i>ndirs-1:
            i=0
    elif cmd[0]=='L':
        i=dir_index-1
        if i<0:
            i=ndirs-1
    dir_index=i
    d=dirs[dir_index]
    if d=='N':
        cy1+=cmd[1]
    elif d=='E':
        cx1+=cmd[1]
    elif d=='S':
        cy1-=cmd[1]
    elif d=='W':
        cx1-=cmd[1]
    if cx!=cx1:
        di=1 if cx1>cx else -1
        steps=list(range(cx+di,cx1,di))
        steps.append(cx1)
        for cx in steps:
            coord=[cx,cy]
            if coord in mem:
                print(abs(cx)+abs(cy))
                exit()
            mem.append(coord)
        cx=cx1
    else:
        di=1 if cy1>cy else -1
        steps=list(range(cy+di,cy1,di))
        steps.append(cy1)
        for cy in steps:
            coord=[cx,cy]
            if coord in mem:
                print(abs(cx)+abs(cy))
                exit()
            mem.append(coord)
        cy=cy1

